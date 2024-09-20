from django.urls import path
from . import views

app_name = 'masterhome' 
urlpatterns = [
    path('', views.index, name='index'),
]
