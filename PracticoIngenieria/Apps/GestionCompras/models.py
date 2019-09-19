from django.db import models

# Create your models here


class Persona(models.Model):
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    Telefono = models.CharField(max_length=25)
    Email = models.CharField(max_length=25)

    def NombreCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.Nombre, self.Apellido)

    def __str__(self):
        return self.NombreCompleto()



class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre


class Compra(models.Model):
    Persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Persona + "compro " + self.Producto