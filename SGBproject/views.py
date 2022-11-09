from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import StaffSignupClass
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView, RedirectView




#The very first page of the bank that seeks user login and allows all users to raise a customer support request
def welcome(request):
    return render(request, 'welcome login.html')


# def index(request):
#     return render(request, 'index.html')


#If the user (Employee) asks to signup
def employee_signup(request):
    if request.method == 'POST':
        fm = StaffSignupClass(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully!! Contact administrator/reporting manager for account privileges.')
            fm.save()
    else:
        fm = StaffSignupClass()
        
    return render(request, 'signup.html', {'form':fm})

# def progress(request):
#     return render(request, 'progress.html ')






