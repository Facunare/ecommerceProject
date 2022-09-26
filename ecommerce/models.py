from django.db import models

# Create your models here.

class stockProducts(models.Model):
    nom_prod = models.CharField(max_length=50)
    cant_prod = models.IntegerField()
    precio_prod = models.FloatField()
    def __str__(self):
        return self.nom_prod