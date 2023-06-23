from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import PocionWikiForm, LoginForm
from .models import PocionWiki

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def servicios(request):
    return render(request, 'Servicios.html')

@login_required
def contacto(request):
    return render(request, 'Contacto.html')
    
# views pociones

@login_required
def respiracionAcuatica(request):
    return render(request, 'RespiracionAcuatica.html')

@login_required
def restaurarSalud(request):
    return render(request, 'RestaurarSalud.html')    
def resistenciaEscarcha(request):
    return render(request, 'ResistenciaEscarcha.html')

@login_required
def resistenciaFuego(request):
    return render(request, 'ResistenciaFuego.html')

@login_required
def resistenciaMagia(request):
    return render(request, 'ResistenciaMagia.html')

@login_required
def resistenciaVeneno(request):
    return render(request, 'ResistenciaVeneno.html')


# Views de crud
@login_required
def verPociones(request):
    pociones = PocionWiki.objects.order_by('id')
    return render(request, 'crud/verPociones.html', {'pociones': pociones})


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

# View del Log In
def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio después del inicio de sesión
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form})

