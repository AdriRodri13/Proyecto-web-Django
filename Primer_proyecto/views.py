import datetime
from django.template import Template,Context

from django.http import HttpResponse

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    #primera vista
    p1 = Persona('Juan','Pedro' )

    doc_externo = open("C:/Users/Admin/PycharmProjects/Primer_proyecto/templates/platilla.html")
    plt =Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"persona":p1})
    documento = plt.render(ctx)
    return HttpResponse(documento)

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

