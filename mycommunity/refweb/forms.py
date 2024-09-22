from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 
        'placeholder': 'Username', 
        'autocomplete': 'off',
    }))
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Name'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user', 
        'placeholder': 'Email Address',
        'autocomplete': 'off',
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 
        'placeholder': 'Password',
        'autocomplete': 'new-password',
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 
        'placeholder': 'Repeat Password',
        'autocomplete': 'off',
    }))


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 
        'placeholder': 'Enter your password',
        'autocomplete': 'new-password',  # 여기에서 autocomplete 설정

    }))

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')
