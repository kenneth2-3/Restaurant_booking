from django.urls import path
from django.shortcuts import render
from .views import book_table, cancel_booking
from . import views

urlpatterns = [
    path('', views.book_table, name='book_table'),
    path("success/<uuid:token>/", views.booking_success, name="booking_success"),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('cancelled/', lambda r: render(r, 'bookings/cancel_success.html'), name='cancel_success'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]
