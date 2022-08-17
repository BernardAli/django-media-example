from django.urls import path
from . import views

urlpatterns = [
    path('', views.media, name='media'),
    path('images/', views.images, name='images'),
]