from django.contrib import admin
from django.urls import path

from FocusFlow import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acceuil/', views.acceuil_views, name='acceuil'),
    path('logout/', views.logout_views, name='logout'),
    path('createProjet/',views.create_projets, name='createProjet'),
    path('showProjet/',views.show_projets, name='showProjet'),
    path('<int:projet_id>/addParticipant/',views.ajouterUser_projets, name='ajouterUser_projets'),
    path('<int:projet_id>/details/', views.detail_projets, name='details'),
    path('showUsers/', views.show_users, name='showUsers'),
    path('createUser/',views.register_user, name='createUser')
]