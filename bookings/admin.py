from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests', 'email')
    list_filter = ('date',)
    search_fields = ('name', 'email')