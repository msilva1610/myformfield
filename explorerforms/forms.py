from django import forms
from . models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('name',)

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('name','category','description','price')
