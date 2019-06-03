from django.db import models

# Create your models here.

class Servant(models.Model):
    Nombre = models.CharField(max_length = 200, null=False)
    Clase = models.CharField(max_length=50, null=False)
    Deck= models.CharField(max_length=5, null=False)
    NoblePhantasm=models.CharField(max_length=50, null= False)