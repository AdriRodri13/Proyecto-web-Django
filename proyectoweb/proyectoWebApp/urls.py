from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='Inicio'),
    path('servicios/', views.services, name='Servicios'),
    path('tienda', views.shop, name='Tienda'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contact, name='Contacto'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)