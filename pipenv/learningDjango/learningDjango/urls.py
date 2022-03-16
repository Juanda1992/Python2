"""learningDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path

#Import apps with its respective view
from miapp import views
from django.conf import settings



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name= "index"), #we inicialice empty to make this the when we start runserver
    path('hola-mundo/',views.hola_mundo, name="hola_mundo"),
    path('inicio/', views.index, name= "inicio"),
    path('pagina/', views.pagina, name= "pagina"),
    path('pagina/<int:redirigir>', views.pagina, name= "pagina"),#Redireeciones
    path('contacto/', views.contacto, name= "contacto"), #we create 3 paths to have optional parameters 
    path('contacto/<str:nombre>/', views.contacto, name= "contacto"),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name= "contacto"), # To be able to send parameters by url we open < and say
    #what kind of parameter we want to send, and then the name of the parameter
    #path('crear-articulo/', views.crear_articulo, name="crear_articulo"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/',views.articulo, name= "articulo"),
    path('editar-articulo/<int:id>/', views.editar_articulo, name ="editar_articulo"),
    path('articulos/', views.articulos, name ="articulos"),
    path('borrar-articulo/ <int:id>/', views.borrar_articulo, name = "borrar_articulo"),
    path('save-article/', views.save_article, name = "save"),
    path('create-article/', views.create_article, name="create"),
    path('create-full-article/', views.create_full_article, name="create_full"),
    # path('file_upload', views.file_upload, name= "file_upload")
   
]

#Configuracion para cambiar el titulo del panel

admin.site.site_header = "Sitio con Django | Juanda"

#Configuracion par cargar imagenes en admin

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
