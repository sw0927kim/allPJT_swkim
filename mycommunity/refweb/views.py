from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
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
    return render(request, 'registration/login.html')
def register(request):
    return render(request, 'registration/register.html')
def forgotpassword(request):
    return render(request, 'registration/forgot-password.html')
def page404(request):
    return render(request, 'error/404.html')
def blankpage(request):
    return render(request, 'Common/blank.html')

def charts(request):
    return render(request, 'Component/charts.html')
def tables(request):
    return render(request, 'Component/tables.html')
