from dataclasses import fields
from tkinter import Widget
from django import forms


# from django import Picture

class FormArticle(forms.Form):

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

