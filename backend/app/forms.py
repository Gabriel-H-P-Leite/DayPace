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
        labels = {
            "first_name": "Primeiro nome",
            "last_name": "Sobrenome",
            "email": "Email",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs.update({
            "placeholder": "Primeiro nome"
        })
        self.fields["last_name"].widget.attrs.update({
            "placeholder": "Sobrenome"
        })
        self.fields["email"].widget.attrs.update({
            "placeholder": "Email"
        })
    def clean(self):
        cleaned_data = super().clean()
        for campo in ["first_name", "last_name", "email"]:
            valor = cleaned_data.get(campo)
            if not valor:
                self.add_error(campo, f"{self.fields[campo].label} é obrigatório.")
            else:
                cleaned_data[campo] = valor.strip().lower()
        return cleaned_data
