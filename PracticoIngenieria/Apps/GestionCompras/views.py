from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from PracticoIngenieria.Apps.GestionCompras.models import Persona, Producto, Compra

def listarPersonas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', context={'personas': personas})

def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'templates/productos.html', context={'productos': productos})

def listarCompras(request):
    compras = Compra.objects.all()
    return render(request, 'compras.html', context={'compras': compras})