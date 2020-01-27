from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def indexView(request):
    return render(request, 'accounts/index.html')

@login_required
def dashboardView(request):
    return render(request, 'accounts/dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration/register.html', {'form':form})

def profileView(request):
	args = {'user' : request.user}
	return render(request, 'accounts/profile.html', args)