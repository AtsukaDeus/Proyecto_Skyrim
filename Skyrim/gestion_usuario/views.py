from django.shortcuts import render, redirect
from .forms import LoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # utilizando los métodos de autenticación de django
from .forms import LoginForm, SignupForm
from django.contrib import messages

# Create your views here.

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

def logOut(request):
    logout(request)
    return redirect('index')

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