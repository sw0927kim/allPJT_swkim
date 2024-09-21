from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')