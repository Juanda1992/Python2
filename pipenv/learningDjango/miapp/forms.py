from dataclasses import fields
import imp
from tkinter import Widget
from django import forms
from django.core import validators #formulario de registro de usuario
from django.contrib.auth.forms import UserCreationForm #formulario de registro de usuario
from django.contrib.auth.models import User

class FormArticle(forms.Form):
    # Este trozo de codigo esta relacionado con dropzone
    def __init__(self, *args, **kwargs):
        super(FormArticle, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'hidden'
      

    title = forms.CharField(
        label = "Titulo"
    )

    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea
        
    )

    file = forms.ImageField(
        label="Imagen",
        required=False,
        
       
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "Publicado ?",
        choices = public_options
    )

    class RegisterForm(UserCreationForm):
        class meta:
            model = User
            fields =['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

