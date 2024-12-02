from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
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
    return render(request, 'create_projet.html')
