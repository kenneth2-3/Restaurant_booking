from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})
