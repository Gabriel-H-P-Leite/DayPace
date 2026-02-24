from django import forms
from django.contrib.auth.models import User

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "caixaTexto"}),
            "last_name": forms.TextInput(attrs={"class": "caixaTexto"}),
            "email": forms.EmailInput(attrs={"class": "caixaTexto"}),
        }
