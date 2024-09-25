from django.urls import path
from . import views

app_name = 'TTTT'

urlpatterns = [
    path('', views.TTTT_home, name='TTTT_home'),
    path('search/', views.search_results, name='search_results'),
]
