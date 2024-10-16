from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('acerca/', views.about),
    path('bienvenido/', views.welcome),
    path('contacto/', views.contact, name='contacto'),
    path('exito/', views.success, name='success'),
    path('testimonio/', views.testimonio, name='testimonio'),
    path('crear_testimonio/', views.crear_testimonio, name='crear_testimonio'),
]
