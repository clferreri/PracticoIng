from django.db import models

# Create your models here


class Persona(models.Model):
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def NombreCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.Nombre, self.Apellido)

    def __str__(self):
        return self.NombreCompleto()


