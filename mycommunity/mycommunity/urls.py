from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('masterhome.urls')),
    path('refweb/', include('refweb.urls')),
    path('board/', include('board.urls')),
    path('TTTT/', include('TTTT.urls')),  # TTTT 앱 등록
]