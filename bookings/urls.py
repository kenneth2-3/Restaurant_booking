from django.urls import path
from django.shortcuts import render
from .views import book_table, cancel_booking
from . import views

urlpatterns = [
    path('', book_table, name='book_table'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('cancel/<uuid:token>/', cancel_booking, name='cancel_booking'),
    path('cancelled/', lambda r: render(r, 'bookings/cancel_success.html'), name='cancel_success'),
]
