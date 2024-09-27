from django.db import models
from db_connection import db

# Create your models here.

calzado_collection = db['Calzado']

class Calzados(models.Model):
    CalzadoId=models.AutoField(primary_key=True)
    CalzadoName = models.CharField(max_length=500)
    CalzadoCodigoBarras = models.CharField(max_length=500)
    CalzadoProveedor = models.CharField(max_length=500)
    CalzadoInversionista = models.CharField(max_length=500)
    CalzadoCantidad = models.IntegerField()
    CalzadoPrecioCompra = models.FloatField()
    CalzadoPrecioVenta = models.FloatField()
    fechaCreate = models.DateTimeField(auto_now_add=True)
    fechaUpdate = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=500)

