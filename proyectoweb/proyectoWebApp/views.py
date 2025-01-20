from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Inicio")

def services(request):
    return HttpResponse("Servicios")

def shop(request):
    return HttpResponse("Tienda")

def blog(request):
    return HttpResponse("Blog")

def contact(request):
    return HttpResponse("Contacto")


