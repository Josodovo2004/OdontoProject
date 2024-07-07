from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=100, null=False)
    sexo = models.CharField(max_length=1, null=False)
    edad = models.IntegerField(null=False)
    celular = models.CharField(max_length=15, null=False)
    documento = models.CharField(max_length=8, null=True)

class Empresa(models.Model):
    nombreEmpresa = models.CharField(max_length=50, null= False)
    ruc = models.CharField(max_length=11, null=False)

class Convenio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

class Consultorio(models.Model):
    numeroConsultorio = models.IntegerField(null=False)

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    pagoDoctor = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    ingresoClinica = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    gasto = models.IntegerField(null=False, validators=[MinValueValidator(0)])

    def costo_total(self):
        return self.pagoDoctor + self.ingresoClinica + self.gasto

    def __str__(self):
        return self.nombre
    
class Tratamiento_Convenio(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    descuento = models.IntegerField(null=False)


class Transaccion(models.Model):
    valorTransaccion = models.IntegerField(null=False)
    fechaTransaccion = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)


class Tratamiento_Transaccion(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

class Rol(models.Model):
    nombre = models.CharField(max_length=50, null=False)

class Empleado(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=100, null=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    fechaHora = models.DateTimeField()
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=1000, null=True)


class Procedimiento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    fechaHora = models.DateTimeField()
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)

class Procedimiento_Tratamiento(models.Model):
    procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.DO_NOTHING)

class Procedimiento_Empleado(models.Model):
    procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)




