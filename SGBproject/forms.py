from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class StaffSignupClass(UserCreationForm):
    password2 = forms.CharField(label = 'Re-type your password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')
        labels = {'email' : 'Email'}
        
  
