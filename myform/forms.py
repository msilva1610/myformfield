from django import forms

from .models import Contato

class ContatoForm(forms.ModelForm):
    class meta:
        model = Contato
        fields = ('nome','endereco')
