from django import http
from django.http.request import HttpHeaders
from django.shortcuts import render
from django.urls import is_valid_path
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from App_Desafio.forms import FormularioFamiliar
from App_Desafio.models import familiar




class homeView():

    def home(self):
        plantilla = get_template('template/index.html')
        return HttpResponse(plantilla.render())
    
    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())
    
    def mod_formulario(self):
        plantilla = get_template('modform.html')
        return HttpResponse(plantilla.render())

    def mod_formulario2(self):
        plantilla = get_template('modform2.html')
        return HttpResponse(plantilla.render())

class FormularioFamiliarView(HttpRequest):

    def index(request):
        familiar= FormularioFamiliar()
        return render(request, "UsuarioIndex.html", {"form":familiar})

    def procesar_formulario(request):
        familiar = FormularioFamiliar(request.POST)
        if familiar.is_valid():
            familiar.save()
            familiar = FormularioFamiliar()
        return render(request,"UsuarioIndex.html", {"form":familiar, "mensaje": "OK"})

    def listar_familiar(request): #devolver datos de la db
        familiares = familiar.objects.all()
        return render(request,'template/listados.html', {"familiares": familiares})



