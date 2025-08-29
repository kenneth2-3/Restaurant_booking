from django.urls import path
from . import views

app_name = "menu"
urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu_list, name='menu_list'),
]
