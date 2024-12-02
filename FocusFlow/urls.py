from django.contrib import admin
from django.urls import path

from FocusFlow import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acceuil/', views.acceuil_views, name='acceuil'),
    path('logout/', views.logout_views, name='logout'),
    path('createProjet/',views.create_projets, name='createProjet'),
    path('showProjet/',views.show_projets, name='showProjet')
]