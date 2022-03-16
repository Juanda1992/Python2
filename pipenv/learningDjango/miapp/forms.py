from dataclasses import fields
from tkinter import Widget
from django import forms


# from django import Picture

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titulo"
    )

    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea
        
    )

    image = forms.ImageField(
        label="Imagen"
       
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "Publicado ?",
        choices = public_options
    )

