from django.db import models

class familiar(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    documento = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    fecha_nacimiento= models.DateField()

    def __str__(self):
      return f"{self.nombre}, {self.apellido},{self.documento},{self.email}, {self.direccion},{self.fecha_nacimiento}, {self.id}"



