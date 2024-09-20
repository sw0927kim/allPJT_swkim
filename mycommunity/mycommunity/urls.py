from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),

    path('board', include('board.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    path('signup/', views.signup, name='signup'),

]