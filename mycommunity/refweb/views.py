from django.shortcuts import render

def index(request):
    return render(request, 'refweb/index.html')

    # Components
def Buttons(request):
    return render(request, 'Component/buttons.html')
def Cards(request):
    return render(request, 'Component/cards.html')

    # Utilities
def Colors(request):
    return render(request, 'utilities/utilities-color.html')
def Borders(request):
    return render(request, 'utilities/utilities-border.html')
def Animations(request):
    return render(request, 'utilities/utilities-animation.html')
def Other(request):
    return render(request, 'utilities/utilities-other.html')

    # Pages
def Login(request):
    return render(request, 'Registration/login.html')
def Register(request):
    return render(request, 'Registration/register.html')
def ForgotPassword(request):
    return render(request, 'Registration/forgot-password.html')
def Page404(request):
    return render(request, 'error/404.html')
def BlankPage(request):
    return render(request, 'Common/blank.html')

def Charts(request):
    return render(request, 'Component/charts.html')
def Tables(request):
    return render(request, 'Component/tables.html')
