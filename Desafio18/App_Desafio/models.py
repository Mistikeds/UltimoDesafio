from django.db import models
from traitlets import default

class familiar(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    documento = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    fecha_nacimiento= models.DateField()



    def __str__(self):
      return f"{self.nombre}, {self.apellido},{self.documento},{self.email}, {self.direccion},{self.fecha_nacimiento}, {self.id}"

class Buscar(familiar, models.Model):
  
 """ documento = models.IntegerField()
  
  def __str__(self):
      return f"{self.nombre}, {self.apellido},{self.documento},{self.email}, {self.direccion},{self.fecha_nacimiento}, {self.id}"""

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=20)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=70, default='')
  

