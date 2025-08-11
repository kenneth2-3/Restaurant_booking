from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logout_success'), name='logout'),
    path('logout_success/', TemplateView.as_view(template_name='accounts/logout_success.html'), name='logout_success'),
]
