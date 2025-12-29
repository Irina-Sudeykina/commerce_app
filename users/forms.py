from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from catalog.forms import StyleFormMixin


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class CustomLoginForm(StyleFormMixin, AuthenticationForm):
    pass
