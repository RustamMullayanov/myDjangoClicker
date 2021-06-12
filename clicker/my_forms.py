from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'inp'}),
            'email': TextInput(attrs={'class': 'inp'}),
            'password1': PasswordInput(attrs={'class': 'inp'}),
            'password2': PasswordInput(attrs={'class': 'inp'})
            }

