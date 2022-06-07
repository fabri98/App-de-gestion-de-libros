from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import libreria
from .forms import LibroForm


def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = libreria.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    form = LibroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'form': form})    

def editar(request,id):
    libro = libreria.objects.get(id=id)
    form = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'form': form})     

def eliminar(request,id):
    libro = libreria.objects.get(id=id)
    libro.delete()
    return redirect('libros')