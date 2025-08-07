from django.shortcuts import render, redirect
from .forms import BookingForm
from django.http import HttpResponseNotFound
from django.contrib import messages
from .models import Booking

# Create your views here.

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bookings/booking_success.html', {'token': Booking.cancel_token})
    else:
        form = BookingForm()
    return render(request, 'bookings/book_table.html', {'form': form})

def cancel_booking(request, token):
    try:
        booking = Booking.objects.get(cancel_token=token)
        if booking.canceled:
            messages.warning(request, "This booking was already cancelled.")
        else:
            booking.canceled = True
            booking.save()
            messages.success(request, "Your booking has been cancelled.")
        return redirect('cancel_success')
    except Booking.DoesNotExist:
        return HttpResponseNotFound("Invalid cancellation link.")