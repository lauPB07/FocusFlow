from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from FocusFlow.models import Projet


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            is_chefProjet = user.groups.filter(name='chef de projet').exists()
            is_admin = user.groups.filter(name='admin').exists()
            if is_admin:
                projets = Projet.objects.all()
            else:
                projets = Projet.objects.filter(user=user)
            context = {
                'projets': projets,
                'is_admin': is_admin,
                'is_chefProjet': is_chefProjet,
            }
            return render(request, 'acceuil.html', context)

        else:
            messages.info(request, 'Identifiant ou mot de passe incorrect')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form })

def acceuil_views(request):
    user = request.user
    is_chefProjet = user.groups.filter(name='chef de projet').exists()
    is_admin = user.groups.filter(name='admin').exists()
    if is_admin:
        projets = Projet.objects.all()
    else:
        projets = Projet.objects.filter(user=user)
    context = {
        'projets': projets,
        'is_admin': is_admin,
        'is_chefProjet': is_chefProjet,
    }
    return render(request, 'acceuil.html', context)

def logout_views(request):
    logout(request)
    return redirect('index')

def create_projets(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        projet = Projet.objects.create(
            nom=nom,
            description=description,
            createdBy=request.user
        )
        projet.user.add(request.user)
        return redirect('acceuil')
    user = request.user
    is_chefProjet = user.groups.filter(name='chef de projet').exists()
    is_admin = user.groups.filter(name='admin').exists()
    context = {
        'is_admin': is_admin,
        'is_chefProjet': is_chefProjet,
    }
    return render(request, 'create_projet.html', context)

def show_projets(request):
    user = request.user
    is_chefProjet = user.groups.filter(name='chef de projet').exists()
    is_admin = user.groups.filter(name='admin').exists()
    if is_admin:
        projets = Projet.objects.all()
    else:
        projets = Projet.objects.filter(createdBy=user)
    context = {
        'projets': projets,
        'is_admin': is_admin,
        'is_chefProjet': is_chefProjet,
    }
    return render(request, 'projets.html', context)

def ajouterUser_projets(request, projet_id):
    user = request.user
    is_chefProjet = user.groups.filter(name='chef de projet').exists()
    is_admin = user.groups.filter(name='admin').exists()
    projet = Projet.objects.get(id=projet_id)

    if request.method == 'POST':
        user_id = request.POST.get('user')
        if user_id:
            user = User.objects.get(id=user_id)


            projet.user.add(user)
            return redirect('showProjet')

    users = User.objects.all()
    return render(request, 'add_participant.html', {
        'projet': projet,
        'users': users,
        'is_admin': is_admin,
        'is_chefProjet': is_chefProjet
    })

def detail_projets(request, projet_id):
    user = request.user
    is_chefProjet = user.groups.filter(name='chef de projet').exists()
    is_admin = user.groups.filter(name='admin').exists()
    projet = Projet.objects.get(id=projet_id)
    context = {
        'projets': projet,
        'is_admin': is_admin,
        'is_chefProjet': is_chefProjet
    }
    return render(request, 'detail_projets.html', context)



