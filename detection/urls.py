# detection/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('url_detection/', views.url_detection, name='url_detection'),
]
