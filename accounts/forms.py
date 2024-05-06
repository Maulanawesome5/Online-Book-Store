from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Merupakan class untuk menampilkan elemen formulir HTML untuk registrasi akun baru.
    Class ini mewarisi (inherit) dari class bawaan Django `UserCreationForm`.
    Formulir default / bawaan yang tersedia adalah:
        - username -> label, input, help text
        - password1 -> label, input, help text
        - password2 -> label, input, help text
    """
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email")
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control mb-2",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control mb-2",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control mb-2",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control mb-2",
                }
            ),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
