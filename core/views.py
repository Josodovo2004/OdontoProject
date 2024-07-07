from rest_framework import generics
from .models import (
    Paciente, Empresa, Convenio, Consultorio, Tratamiento, Tratamiento_Convenio,
    Transaccion, Tratamiento_Transaccion, Rol, Empleado, Cita, Procedimiento,
    Procedimiento_Tratamiento, Procedimiento_Empleado
)
from .serializers import (
    PacienteSerializer, EmpresaSerializer, ConvenioSerializer, ConsultorioSerializer, TratamientoSerializer,
    TratamientoConvenioSerializer, TransaccionSerializer, TratamientoTransaccionSerializer,
    RolSerializer, EmpleadoSerializer, CitaSerializer, ProcedimientoSerializer,
    ProcedimientoTratamientoSerializer, ProcedimientoEmpleadoSerializer
)

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# Empresa Views
class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

# Convenio Views
class ConvenioListCreateView(generics.ListCreateAPIView):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer

class ConvenioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer

# Consultorio Views
class ConsultorioListCreateView(generics.ListCreateAPIView):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer

class ConsultorioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer

# Tratamiento Views
class TratamientoListCreateView(generics.ListCreateAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class TratamientoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

# Tratamiento_Convenio Views
class TratamientoConvenioListCreateView(generics.ListCreateAPIView):
    queryset = Tratamiento_Convenio.objects.all()
    serializer_class = TratamientoConvenioSerializer

class TratamientoConvenioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tratamiento_Convenio.objects.all()
    serializer_class = TratamientoConvenioSerializer

# Transaccion Views
class TransaccionListCreateView(generics.ListCreateAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class TransaccionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

# Tratamiento_Transaccion Views
class TratamientoTransaccionListCreateView(generics.ListCreateAPIView):
    queryset = Tratamiento_Transaccion.objects.all()
    serializer_class = TratamientoTransaccionSerializer

class TratamientoTransaccionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tratamiento_Transaccion.objects.all()
    serializer_class = TratamientoTransaccionSerializer

# Rol Views
class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

# Empleado Views
class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

# Cita Views
class CitaListCreateView(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

# Procedimiento Views
class ProcedimientoListCreateView(generics.ListCreateAPIView):
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer

class ProcedimientoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer

# Procedimiento_Tratamiento Views
class ProcedimientoTratamientoListCreateView(generics.ListCreateAPIView):
    queryset = Procedimiento_Tratamiento.objects.all()
    serializer_class = ProcedimientoTratamientoSerializer

class ProcedimientoTratamientoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedimiento_Tratamiento.objects.all()
    serializer_class = ProcedimientoTratamientoSerializer

# Procedimiento_Empleado Views
class ProcedimientoEmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Procedimiento_Empleado.objects.all()
    serializer_class = ProcedimientoEmpleadoSerializer

class ProcedimientoEmpleadoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedimiento_Empleado.objects.all()
    serializer_class = ProcedimientoEmpleadoSerializer