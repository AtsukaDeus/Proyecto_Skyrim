from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from .forms import PocionWikiForm, LoginForm
from .models import PocionWiki

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # utilizando los métodos de autenticación de django
from .forms import LoginForm, SignupForm
from django.contrib import messages

# Importaciones para la API
from rest_framework import generics
from .serializers import PocionWikiSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')


def servicios(request):
    return render(request, 'Servicios.html')


def contacto(request):
    return render(request, 'Contacto.html')
    
# views pociones


def respiracionAcuatica(request):
    return render(request, 'RespiracionAcuatica.html')


def restaurarSalud(request):
    return render(request, 'RestaurarSalud.html')   

def resistenciaEscarcha(request):
    return render(request, 'ResistenciaEscarcha.html')


def resistenciaFuego(request):
    return render(request, 'ResistenciaFuego.html')


def resistenciaMagia(request):
    return render(request, 'ResistenciaMagia.html')


def resistenciaVeneno(request):
    return render(request, 'ResistenciaVeneno.html')


# ------------------------ Views de crud ----------------------------------
@login_required
def verPociones(request):
    return render(request, 'crud/verPociones.html')


@login_required
def crearPociones(request):
    if request.method == 'POST':
        form = PocionWikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_pociones')
    else:
        form = PocionWikiForm()
    
    return render(request, 'crud/crearPocion.html', {'form': form})

@login_required
def editarPociones(request, id):
    pocion = get_object_or_404(PocionWiki, pk=id)
    if request.method == 'POST':
        formPocionWiki = PocionWikiForm(request.POST, instance=pocion)
        if formPocionWiki.is_valid():
            formPocionWiki.save()
            return redirect('ver_pociones')
    else:
        formPocionWiki = PocionWikiForm(instance=pocion)
        
    return render(request, 'crud/editarPocion.html', {'formPocionWiki': formPocionWiki}) 


@login_required
def eliminarPociones(request, id):
    pocion = get_object_or_404(PocionWiki, pk=id)
    if pocion:
        pocion.delete()
    
    return redirect('ver_pociones')

#---------------------------------------------------------------------------------


# View del Log In
def logIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form})

# view del Log Out
def logOut(request):
    logout(request)
    return redirect('index')


# view del Sign Up
def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario registrado exitosamente! Por favor, inicia sesión.')
            return redirect('login')  
    else:
        form = SignupForm()
    
    return render(request, 'login/signup.html', {'form': form})


# ---------------  class view API --------------------
@method_decorator(login_required, name='dispatch')
class PocionWikiList(generics.ListCreateAPIView):
    queryset = PocionWiki.objects.all()
    serializer_class = PocionWikiSerializer

