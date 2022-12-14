from distutils.command.upload import upload
from email.policy import default
from django.db import models


# Create your models here.
class categorias(models.Model):
    nombre_cat = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    def __str__(self) -> str:
            return self.nombre_cat
            
class stockProducts(models.Model):
    image_prod = models.ImageField(upload_to='ecommerce/photos')
    nom_prod = models.CharField(max_length=50)
    cant_prod = models.IntegerField()
    precio_prod = models.FloatField()   
    descripcion = models.TextField(max_length=250)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nom_prod

class carrito(models.Model):
    nom_prod = models.CharField(max_length=50)
    cant_prod = models.IntegerField()
    precio_prod = models.FloatField()
    def __str__(self) -> str:
        return self.nom_prod