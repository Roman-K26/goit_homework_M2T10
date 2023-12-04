from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = "app_photo"

urlpatterns = [
    path('', views.index, name='home') # app_photo:home
]