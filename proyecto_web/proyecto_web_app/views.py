from django.shortcuts import render, HttpResponse

# Create your views here.

#Vista de inicio
def home(request):
    return HttpResponse("Inicio")

#Vista de servicios
def services(request):
    return HttpResponse("Servicios")

#Vista de tienda
def shop(request):
    return HttpResponse("Tienda")

#Vista de blog
def blog(request):
    return HttpResponse("Blog")

#Vista de contacto
def contact(request):
    return HttpResponse("Contacto")
