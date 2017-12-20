from django.shortcuts import render, redirect
from . forms import CategoriaForm, ProdutoForm

# Create your views here.

def home(request):
    return render(request,'explorerforms/home.html')

def categoria(request):
    if request.POST:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria')
    else:
        form = CategoriaForm()
        return render (request, 'explorerforms/categoria.html', {'form': form})

def produto(request):
    if request.POST:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('produto')
    else:
        form = ProdutoForm()
    return render (request,'explorerforms/produtos.html', {'form': form})
