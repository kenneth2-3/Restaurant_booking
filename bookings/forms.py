from django import forms
from .models import Booking
from django.utils import timezone


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

        # Block today and past dates in the frontend
        tomorrow = timezone.localdate() + timezone.timedelta(days=1)
        self.fields['date'].widget.attrs['min'] = tomorrow.strftime('%Y-%m-%d')

        # Keep all time slots selectable (today is blocked)
        self.fields['time'].choices = Booking.TIME_PERIODS

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            # Prevents duplicate bookings
            if Booking.objects.filter(date=date, time=time).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Sorry, a booking already exists for that time.")
        return cleaned_data
