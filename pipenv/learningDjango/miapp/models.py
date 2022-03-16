from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField( max_length=150, verbose_name="Titulo")
    content = models.TextField()
    image = models.ImageField( default='null',upload_to= "articles")
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id']
        #Different ways to order 
        #['public'],['-public'],['created_at'],['']
        #verbose_name also could be use as a parameter in the properties in the classes
        #lets check an example in class article, title will be become in Titulo     

        #We can also change the name of our app going to apps and use the verbose_name
        #then go to settings and add an extension to able to be read it this addition in
        #this ocassion would be .apps.MiappConfig (In installed app)

    #MAGIC METHOD TO PRINT OBJECTS
    def __str__(self):

        if self.public:
            public = "(Publicado)"
        else:
            public = "(Privado)"   
            
        return f"{self.title} {public}"

# class Picture (models.Model):
#     imagen = models.ImageField("Imagen", upload_to='articles')
# class Image(models.Model):
#     image = models.ImageField(upload_to="articles")
#     date = models.DateTimeField( auto_now_add=True)

#     class Meta:
#         ordering=['-date']

#     def __str__(self):
#         return str(self.date)
   
class Category(models.Model) :   
    name= models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-id']