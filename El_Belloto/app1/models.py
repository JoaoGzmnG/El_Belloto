from django.db import models

# Create your models here.

#Clase usuarios. Tendría que modificar auth y no quiero hacerlo aun. Prefiero utilizar clase de Django. 
'''
class User1(models.Model):
    username = models.CharsField(max_length=200)
    password = models.CharsField(max_length=200)
'''

class Pendiente(models.Model):
    categoria_pendiente = models.CharField(max_length=200)
    descripcion_pendiente = models.CharField(max_length=200)
    tiempo_destinado = models.IntegerField(default=0)
    #pub_date = models.DateTimeField('date published')


class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    sector_ln = models.CharField(max_length=200)

