from django.shortcuts import render

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import ContatoForm

# Create your views here.
def home(request):
    return render (request,'myform/home.html')

def contato(request):
    form = None
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return render ('myform/home.html')
    else:
        pass
        form = ContatoForm()
    return render (request, 'myform/contatoform.html', {'form': form} )

def about(request):
    return render (request, 'myform/about.html')
