from django import forms
from .models import PocionWiki
from .models import PocionWiki
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PocionWikiForm(forms.ModelForm):
    class Meta:
        model = PocionWiki
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre Poción'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingredientes, Ej: Ramita de Cardo, Mirriam de Escarcha'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre de usuario'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña'
        })
    )
    
    
class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre de usuario'
        })
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña'
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
