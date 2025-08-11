from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after register
            return redirect('home')  # change 'home' to your homepage URL name
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
