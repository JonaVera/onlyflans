# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.hola),
#     path('text/', views.hola_text),
#     path('json/', views.hola_json),
#     path('template/', views.hola_template),
# ]

###########################################################
from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.acerca),
    path('welcome/', views.inicio),
]