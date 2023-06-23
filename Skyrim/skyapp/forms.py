from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import PocionWiki
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Field
from .models import PocionWiki

class PocionWikiForm(forms.ModelForm):
    class Meta:
        model = PocionWiki
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)