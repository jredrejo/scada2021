from django.db import models
from django.utils import timezone

# Create your models here.


tipos_datos = (
    ("I", "Integer"),
    ("F", "Float"),
    ("b", "Bit"),
    ("B", "Byte"),
    ("W", "Word"),
    ("DW", "Double_Word"),
)


class Tags(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=tipos_datos)

    def __str__(self):
        return "{}-{}".format(self.nombre, self.direccion)


class Valores(models.Model):
    valor = models.FloatField(null=True)
    fecha = models.DateTimeField(default=timezone.now)
    tag = models.ForeignKey(Tags, related_name="tags", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.valor)
