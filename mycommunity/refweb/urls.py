from django.urls import path
from . import views

app_name = 'refweb' 
urlpatterns = [
    path('', views.index, name='index'),

    # Components
    path('Buttons/', views.Buttons, name='refweb_Buttons'),
    path('Cards/', views.Cards, name='refweb_Cards'),
    # Utilities
    path('Colors/', views.Colors, name='refweb_Colors'),
    path('Borders/', views.Borders, name='refweb_Borders'),
    path('Animations/', views.Animations, name='refweb_Animations'),
    path('Other/', views.Other, name='refweb_Other'),
    # Pages
    path('Login/', views.Login, name='refweb_Login'),
    path('Register/', views.Register, name='refweb_Register'),
    path('ForgotPassword/', views.ForgotPassword, name='refweb_ForgotPassword'),
    path('Page404/', views.Page404, name='refweb_Page404'),
    path('BlankPage/', views.BlankPage, name='refweb_BlankPage'),

    path('Charts/', views.Charts, name='refweb_Charts'),
    path('Tables/', views.Tables, name='refweb_Tables'),
]
