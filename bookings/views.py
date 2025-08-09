from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from django.http import HttpResponseNotFound
from django.contrib import messages
from .models import Booking
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Don't save to DB yet
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            return render(request, 'bookings/booking_success.html', {'token': booking.cancel_token})
    else:
        form = BookingForm()
    
    return render(request, 'bookings/book_table.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

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
    
@staff_member_required
def manage_bookings(request):
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(request, 'bookings/manage_bookings.html', {'bookings': bookings})

@staff_member_required
def cancel_booking_admin(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.canceled = True
    booking.save()
    messages.success(request, f"Booking for {booking.name} on {booking.date} has been cancelled.")
    return redirect('manage_bookings')