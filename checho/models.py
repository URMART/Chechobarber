from django.db import models

# Create your models here.
class Servicios(models.Model):
    nombreServicio=models.CharField(max_length=255)
    precio=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.nombreServicio

class Clientes(models.Model):

    nombre=models.CharField(max_length=100)       
    apellido=models.CharField(max_length=100)       
    numeroTelefono=models.PositiveIntegerField()
    usuario=models.CharField(max_length=100)       
    contraseña=models.CharField(max_length=100)
    rol=models.CharField(max_length=100,default="cliente")


    def __str__(self) -> str:

        return f" {self.nombre} {self.apellido}  "


class Administradores(models.Model):

    nombre=models.CharField(max_length=100)       
    apellido=models.CharField(max_length=100)       
    numeroTelefono=models.PositiveIntegerField()
    usuario=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=100)
    rol=models.CharField(max_length=100,default="administrador")

    def __str__(self) -> str:

        return f" {self.nombre} {self.apellido}  "        

class Empleados(models.Model):

    nombre=models.CharField(max_length=100)       
    apellido=models.CharField(max_length=100)       
    numeroTelefono=models.PositiveIntegerField()
    usuario=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=100)
    rol=models.CharField(max_length=100,default="empleado")
    administrador=models.ForeignKey(Administradores,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:

        return f" {self.nombre} {self.apellido}  "

class Citas(models.Model):

    fecha=models.DateField(auto_now_add=False)
    hora=models.TimeField(auto_now_add=False)
    estado=models.BooleanField(default=True)
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE,null=True)
    servicio=models.ForeignKey(Servicios, on_delete=models.CASCADE,null=True)
    empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE,null=True)


    def __str__(self):

        return  f"   {self.fecha} {self.hora} {self.cliente}"