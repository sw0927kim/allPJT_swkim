from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
def index(request):
    return render(request, 'masterhome/index.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('masterhome:index')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')  # 'id' 대신 'username' 사용
            user.first_name = form.cleaned_data.get('name')  # 'name' 필드를 'first_name'에 저장
            user.save()
            return redirect('masterhome:index')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})