from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm
app_name = 'refweb' 
urlpatterns = [
    path('', views.index, name='index'),

    # Components
    path('buttons/', views.buttons, name='refweb_buttons'),
    path('cards/', views.cards, name='refweb_cards'),
    # Utilities
    path('colors/', views.colors, name='refweb_colors'),
    path('borders/', views.borders, name='refweb_borders'),
    path('animations/', views.animations, name='refweb_animations'),
    path('other/', views.other, name='refweb_other'),
    # Pages
    path('login/', auth_views.LoginView.as_view(
    template_name='registration/refweb_login.html', 
    authentication_form=CustomAuthenticationForm), 
    name='refweb_login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # 소문자로 변경

    
    path('register/', views.register, name='refweb_register'),
    path('page404/', views.page404, name='refweb_page404'),
    path('blankPage/', views.blankpage, name='refweb_blankpage'),

    path('charts/', views.charts, name='refweb_charts'),
    path('tables/', views.tables, name='refweb_tables'),
]
