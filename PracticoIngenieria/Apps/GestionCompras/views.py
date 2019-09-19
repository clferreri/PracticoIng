from django.shortcuts import render, render_to_response

from PracticoIngenieria.Apps.GestionCompras.models import Persona, Producto, Compra

def listarPersonas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', context={'personas': personas})
