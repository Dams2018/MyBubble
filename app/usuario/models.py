from django.db import models

# Create your models here.

class Persona(models.Model):
    rut=models.CharField(max_length=12, primary_key=True)
