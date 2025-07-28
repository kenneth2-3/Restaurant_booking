from django.contrib import admin
from .models import MenuItem

# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name',)
