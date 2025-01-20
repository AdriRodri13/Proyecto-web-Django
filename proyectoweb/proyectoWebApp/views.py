from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "proyectoWebApp/home.html")

def services(request):
    return render(request, "proyectoWebApp/Servicios.html")

def shop(request):
    return render(request, "proyectoWebApp/Tienda.html")

def blog(request):
    return render(request, "proyectoWebApp/Blog.html")

def contact(request):
    return render(request, "proyectoWebApp/Contacto.html")


