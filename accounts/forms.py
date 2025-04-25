from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.
                PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.
                PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'Usuario', 'first_name': 'Primer nombre', 
                'last_name': 'Apellidos', 'email': 'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control '}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control '}),
            'email':forms.EmailInput(attrs={'class':'form-control '})
            }

class LoginForm(AuthenticationForm):
    username = UsernameField(
            label=_("Nombre de usuario"),
            widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control p-2"})
        )
    password = forms.CharField(
        label=_("Contraseña"), strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"form-control p-2"}),
    )
    