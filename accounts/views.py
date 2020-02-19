from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic import ListView
from accounts.models import AccountM
from accounts.tables import AccountTable
from django_tables2 import SingleTableView


def indexView(request):
    return render(request, 'accounts/index.html')

@login_required
def dashboardView(request):
    return render(request, 'accounts/dashboard.html')
class AccountMList(ListView):
    model = AccountM

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
    
class AccountsListView(SingleTableView):
    model = AccountM
    template_name = 'accounts/accountm.html'
    table_class = AccountTable
