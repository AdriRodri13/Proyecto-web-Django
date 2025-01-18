import datetime
from django.template import Template,Context
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    #primera vista
    p1 = Persona('Juan','Pedro' )

    return render(request,"platilla.html",{'persona':p1})

def despedida(request):
    return HttpResponse("<h1>Hasta luego</h1>")

def dame_fecha(request):
    fecha = datetime.datetime.now()
    documento = "<h1>%s</h1>" % fecha
    return HttpResponse(documento)

def calcula_edad(request, year):
    edad_actual = 18
    periodo = year - 2025
    edad_futura = edad_actual + periodo
    documento = "<h1>En el año %s tendras %s años</h1>" %(year, edad_futura)
    return HttpResponse(documento)

def herencia (request):
    return render(request, "pruebaHerencia.html")
