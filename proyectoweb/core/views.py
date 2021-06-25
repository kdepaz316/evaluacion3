def home(request): 
    return render(request,'core/home.html')


from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def registro(request):

    return render(request, 'core/registro.html')

def personas(request):
    personas=Persona.objects.all()
    datos={
        'personas':personas
    }

    return render(request, 'core/personas.html', datos)

def form_persona(request):
    datos = {
        'form': PersonaForm()
    }
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "persona ingresada"
    

    return render(request, 'core/form_persona.html', datos)

def form_mod_persona(request, id):
    personas = Persona.objects.get(Id=id)
    datos = {
        'form': PersonaForm(data=request.POST, instance=personas)
    }
    if request.method == 'POST':
        formulario = PersonaForm(data=request.POST, instance=personas)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos modificados"
    return render(request, 'core/form_mod_persona.html', datos)

def form_del_persona(request,id):
    persona = Persona.objects.get(Id=id)
    persona.delete()
    return redirect(to=personas)