from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil
from .models import Avaliacao

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Nome de usuário',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Senha',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar senha',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefone', 'rua', 'numero', 'bairro', 'cidade', 'complemento', 'cep']
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta: 
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.RadioSelect(attrs={'class': 'rating-input'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'compartilhe a sua experiência...'
        })
    }