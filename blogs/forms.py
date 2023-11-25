from django import forms
from .models import *


class FormularioArticulo(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = "__all__"