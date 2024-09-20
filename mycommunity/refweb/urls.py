from django.urls import path
from . import views

app_name = 'refweb' 
urlpatterns = [
    path('', views.index, name='index'),

    # Components
    path('Buttons/', views.Buttons, name='Buttons'),
    path('Cards/', views.Cards, name='Cards'),
    # Utilities
    path('Colors/', views.Colors, name='Colors'),
    path('Borders/', views.Borders, name='Borders'),
    path('Animations/', views.Animations, name='Animations'),
    path('Other/', views.Other, name='Other'),
    # Pages
    path('Login/', views.Login, name='Login'),
    path('Register/', views.Register, name='Register'),
    path('ForgotPassword/', views.ForgotPassword, name='ForgotPassword'),
    path('Page404/', views.Page404, name='Page404'),
    path('BlankPage/', views.BlankPage, name='BlankPage'),

    path('Charts/', views.Charts, name='Charts'),
    path('Tables/', views.Tables, name='Tables'),
]
