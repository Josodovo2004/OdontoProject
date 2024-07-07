from rest_framework import serializers
from .models import (
    Paciente, Empresa, Convenio, Consultorio, Tratamiento, Tratamiento_Convenio,
    Transaccion, Tratamiento_Transaccion, Rol, Empleado, Cita, Procedimiento,
    Procedimiento_Tratamiento, Procedimiento_Empleado
)

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = '__all__'

class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    costo_total = serializers.SerializerMethodField()

    class Meta:
        model = Tratamiento
        fields = '__all__'

    def get_costo_total(self, obj):
        return obj.costo_total()

class TratamientoConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento_Convenio
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'

class TratamientoTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento_Transaccion
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class ProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento
        fields = '__all__'

class ProcedimientoTratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento_Tratamiento
        fields = '__all__'

class ProcedimientoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento_Empleado
        fields = '__all__'
