from django.contrib import admin
from django.urls import path

from FocusFlow import views

urlpatterns = [
    path('', views.index),
]