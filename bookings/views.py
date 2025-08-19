from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from django.http import HttpResponseNotFound
from django.contrib import messages
from .models import Booking
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'bookings/booking_success.html', {'token': booking.cancel_token})
    else:
        form = BookingForm()
    
    return render(request, 'bookings/book_table.html', {'form': form})

@login_required
def booking_success(request, token):
    return render(request, "bookings/booking_success.html", {"token": token})

@login_required
def my_bookings(request):
    bookings = request.user.bookings.all().order_by('-date', '-time')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, token):
        booking = get_object_or_404(Booking, cancel_token=token, user=request.user)
        if booking.is_cancelled:
            messages.warning(request, "This booking was already cancelled.")
        else:
            booking.is_cancelled = True
            booking.save()
            messages.success(request, "Your booking has been cancelled.")
        return redirect('cancel_success')

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