from django.shortcuts import render, redirect
from .forms import FormularioContacto
from  django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    formulario = FormularioContacto()
    if request.method == "POST":
        formulario = FormularioContacto(data = request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage("Mensaje dede App Django",
                                 "El usuario con nombre {} con la direccion {} te escribe lo siguiente: \n\n{}".format(nombre,email,contenido),
                                 "", ["daniadri963@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

    return render(request, "contacto/contacto.html", {"formulario": formulario})
