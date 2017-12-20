from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from . models import Document
from . forms import DocumentForm

# Create your views here.
def home(request):
    if request.POST:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('uploaded')
    else:
        form = DocumentForm()
    return render (request, 'upload/home.html', {'form': form})
def uploaded(request):
    documents = Document.objects.all()
    return render(request, 'upload/uploaded.html',{'documents': documents})
