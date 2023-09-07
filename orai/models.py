from django.db import models

# Create your models here.

class Orai(models.Model):
    miestas = models.CharField(max_length=255)
    temperatura = models.FloatField()
    aprasymas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
