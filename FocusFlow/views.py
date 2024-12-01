from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            print(user)
            return redirect('acceuil')
        else:
            messages.info(request, 'Identifiant ou mot de passe incorrect')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def acceuil_views(request):
    return render(request, 'acceuil.html')

def logout_views(request):
    logout(request)
    return redirect('index')