from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .forms import CustomUserCreationForm
from django.contrib import messages

def group_check(user):
    return user.groups.filter(name='ButtonAccessGroup').exists()

def index(request):
    return render(request, 'refweb/index.html')

def buttons(request):
    if not group_check(request.user):
        return HttpResponseForbidden("해당 페이지에 대한 권한이 없습니다. 관리자에게 문의하세요!.")
    return render(request, 'Component/buttons.html')

def cards(request):
    return render(request, 'Component/cards.html')

    # Utilities
def colors(request):
    return render(request, 'utilities/utilities-color.html')
def borders(request):
    return render(request, 'utilities/utilities-border.html')
def animations(request):
    return render(request, 'utilities/utilities-animation.html')
def other(request):
    return render(request, 'utilities/utilities-other.html')

    # Pages
def login(request):
    return render(request, 'registration/refweb_login.html')

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
    return render(request, 'registration/refweb_register.html', {'form': form})

def page404(request):
    return render(request, 'error/404.html')
def blankpage(request):
    return render(request, 'Common/blank.html')

def charts(request):
    return render(request, 'Component/charts.html')
def tables(request):
    return render(request, 'Component/tables.html')
