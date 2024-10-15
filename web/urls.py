from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('acerca/', views.about),
    path('bienvenido/', views.welcome),
]
