from django import forms
from .models import Booking
from django.utils import timezone
from datetime import date as dt_date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        guests = cleaned_data.get('guests')

        # to prevent picking past dates
        if date and date < dt_date.today():
            self.add_error('date', "You cannot select a past date.")

        # to prevent duplicate bookings
        if Booking.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError("Sorry, a booking already exists for that time.")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Frontend restriction: block past dates
        today = timezone.localdate()  # Django's timezone-aware current date
        self.fields['date'].widget.attrs['min'] = today.strftime('%Y-%m-%d')

        # Set minimum time for today (frontend only)
        now_time = timezone.localtime().strftime('%H:%M')
        self.fields['time'].widget.attrs['min'] = now_time