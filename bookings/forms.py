from django import forms
from .models import Booking
from django.utils import timezone
from datetime import date as dt_date, datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(), 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # To block past dates
        today = timezone.localdate()
        self.fields['date'].widget.attrs['min'] = today.strftime('%Y-%m-%d')

        # To disable past time slots for today
        now_time = timezone.localtime().time()
        time_choices = []
        for idx, label in Booking.TIME_PERIODS:
            slot_start = datetime.strptime(label.split('-')[0], "%H:%M").time()
            if self.initial.get('date') == today:
                if slot_start >= now_time:
                    time_choices.append((idx, label))
            else:
                time_choices.append((idx, label))
        self.fields['time'].choices = time_choices

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # To prevent past dates
        if date and date < dt_date.today():
            self.add_error('date', "You cannot select a past date.")

        # To prevent past time for today
        if date == dt_date.today() and time is not None:
            slot_label = dict(Booking.TIME_PERIODS)[time]
            slot_start = datetime.strptime(slot_label.split('-')[0], "%H:%M").time()
            if slot_start < timezone.localtime().time():
                self.add_error('time', "You cannot select a past time today.")

        # To prevent duplicate bookings
        if date and time and Booking.objects.filter(date=date, time=time).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Sorry, a booking already exists for that time.")

        return cleaned_data

    def clean_guests(self):
        guests = self.cleaned_data.get('guests')
        if guests > 5:
            raise forms.ValidationError("You can only book up to 5 guests per table.")
        if guests < 1:
            raise forms.ValidationError("You must book at least 1 guest.")
        return guests
