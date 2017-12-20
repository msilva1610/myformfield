from django.shortcuts import render, redirect
from . forms import NomeForm

# Create your views here.
def home(request):
    if request.POST:
        form = NomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # nome da url
    else:
        form = NomeForm()
    return render(request,'livro/home.html', {'form': form})
