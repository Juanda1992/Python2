
from email.mime import image
import imp
from re import A, X
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from isort import file

from miapp.models import Article
from miapp.forms import FormArticle
from django.contrib import messages
import os


#Formulario para creacion de usuarios
from django.contrib.auth.forms import UserCreationForm 
# from miapp.forms import RegisterForm


# Create your views here.
#MVC = Modelo Vista Controlador
#MVT = Modelo Template Vista (En este caso la vista es el controlador)-> Acciones y metodos

layout ="""
"""



def index(request):
    nombre = 'JuandaOG'
    lenguajes =['Java', 'PHP','JavaScript']

    year =2021
    hasta = range(year,2051)
   
    return render( request, 'index.html',{
        'title': 'Inicio pasando datos',
        'mi_variable': 'Soy u dato que esta en la vista',
        'nombre' : nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):
        return render(request,'hola_mundo.html')

        #To be able to see this u need to charge this into in a url so
        #go to urls.py

        #examples of more variables

    #exampe of redirections
def pagina (request, redirigir=0):  

    if redirigir ==1:
        return redirect('/inicio/')

    return render(request, 'pagina.html')  
# Function to pick up parameter by Url

# we inicialized the parameters empty to be able to work,
#and then to dont obligate the function to work with it
#we create a conditional to be able to work in every case

def contacto (request,nombre ="" ,apellido =""):

     html=""

     if nombre and apellido:
         html += "<p>El nombre completo es </p>"
         html += f"<h3> {nombre} {apellido}</h3> "

     return  HttpResponse(layout+f"<h2>Contacto</h2>" + html)   

def crear_articulo(request, title, content, public, image):

    articulo = Article(
        title = title,
        content = content,
        image = image,
        public = public
    )

    articulo.save()

    return HttpResponse(f'Articulo creado {articulo.title}')     

def articulo(request):

    try:
        articulo = Article.objects.get(title ="primer articulo", public =True)
        #Utilizamos objects para acceder a los modelos y objetos de la DB
        response = f"Articulo : { articulo.title }" 

    except:

        response = "<h2> Articulo no encontrado </h2>"  
        return HttpResponse (response)  

def save_article(request):

    if request.method == 'POST':
        
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        image = request.FILES.get('file')

        #Recoger los datos enviados por el formulario
        articulo = Article(         
            title = title,
            content = content,
            public = public,
            image = image
        )

        articulo.save()

        messages.success(request, "Tu articulo ha sido creado exitosamente :D")  
        return redirect('/articulos/')
        #return HttpResponse(f'Articulo creado {articulo.title}')
        
    else:
        return HttpResponse("<h2>No se pudo crear el articulo</h2>")  

def create_article(request):

    return render(request, 'create_article.html')   

def create_full_article(request): 

    if request.method == 'POST':

        formulario = FormArticle(request.POST, files=request.FILES)   

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form ['public']
            image = data_form ['image']

            #Recoger los datos enviados por el formulario
            articulo = Article(         
                title = title,
                content = content,
                public = public,
                image = image
            )
            
            articulo.save()
            
            messages.success(request, "Creado")  
            return redirect('articulos')
            
            #return HttpResponse(title)

        else:
            formulario = FormArticle()    

    formulario = FormArticle()
     
    return render(request, 'create_full_article.html',{
        'form': formulario 
    })
    
def editar_articulo(request, id):


    articulo = Article.objects.get(pk=id)    

    articulo.title = "Updated Tercer"
    articulo.content = "Content updated"
    articulo.image = ""
    articulo.public = False
    
    articulo.save()
    

    return HttpResponse (f'Articulo editado {articulo.title}') 

def articulos (request):

    articulos = Article.objects.filter(public=True)
    
    articulos = Article.objects.all()

    articulos = Article.objects.filter()
        
    
    return render (request, 'articulos.html',{
        'articulos': articulos
    })

def borrar_articulo(request, id,image):

    articulo = Article.objects.get(pk=id)   
    #os.remove() 
    articulo.delete()
    os.remove(image)
    
    
    messages.success(request, "Tu articulo ha sido eliminado exitosamente :S")
    return redirect('articulos')

def register_page(request):  

    register_form= UserCreationForm();

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save() 

            return redirect('inicio')

    return render(request, 'register.html',{
        'register_form' :register_form
    }) 

def remove_article():
    archivoborrar = 'media/articles'
    if os.path.exists(f'{archivoborrar}.jpg'):
        os.remove(f'{archivoborrar}')