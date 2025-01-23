from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "proyectoWebApp/home.html")


def shop(request):
    return render(request, "proyectoWebApp/Tienda.html")


def contact(request):
    return render(request, "proyectoWebApp/Contacto.html")


