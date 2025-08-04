from django import forms
from .models import Booking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        guests = cleaned_data.get('guests')

        # Example: prevent duplicate bookings
        if Booking.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError("Sorry, a booking already exists for that time.")
