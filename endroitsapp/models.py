from django.db import models

# Create your models here.
class Endroits(models.Model):
    nom =models.CharField(max_length=200)
    description=models.CharField(max_length=2085)
    adresse=models.CharField(max_length=200, blank=True)
    email=models.CharField(max_length=200, blank=True)
    reseaux_sociaux=models.CharField(max_length=200 , blank=True)
    url1 =models.CharField(max_length=2085)
    url2 = models.CharField(max_length=2085)
    url3 = models.CharField(max_length=2085)
    url4 = models.CharField(max_length=2085)
    telephone= models.CharField(max_length=200, blank=True)
    longitude = models.FloatField()
    latitude =  models.FloatField()

def __str__(self):
    return self.nom
