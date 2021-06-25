from django.db import models

# Create your models here.

class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id de tipo')
    nombreTipo = models.CharField(max_length=50, verbose_name='Nombre de Tipo')
    
    def __str__(self):
        return self.nombreTipo

class Persona(models.Model):
    Id = models.IntegerField(primary_key=True, verbose_name='Id de persona')
    Rut = models.CharField(max_length=12, verbose_name='rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre de persona')
    apellido = models.CharField(max_length=50, verbose_name='apellido de persona')
    categoria = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.Rut