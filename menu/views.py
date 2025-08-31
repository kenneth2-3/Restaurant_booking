from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MenuItem

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='account_login')  
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})
