from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from dashboard.models import *
from .serializers import *
from rest_framework.decorators import action
# Create your views here.

class CuentaView(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnosSerializer

class ProfesorView(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesoresSerializer

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer

class AsistenciaView(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciasSerializer

class NotaView(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotasSerializer
    

class InscripcionView(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionesSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        alumno_id = self.request.query_params.get('alumno')
        if alumno_id:
            queryset = queryset.filter(alumno=alumno_id)
        return queryset

class KeyAlumnoView(viewsets.ModelViewSet):
    queryset = KeyAlumno.objects.all()
    serializer_class = KeyAlumnosSerializer

class ObtenerInscripcionesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InscripcionesSerializer

    def get_queryset(self):
        alumno_id = self.kwargs['alumno_id']
        return Inscripcion.objects.filter(alumno=alumno_id)
    
class NotaByAlumnoAndCursoView(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotasSerializer

    def get_queryset(self):
        alumno_id = self.request.query_params.get('alumno')
        curso_id = self.request.query_params.get('curso')

        if alumno_id and curso_id:
            return Nota.objects.filter(alumno=alumno_id, curso=curso_id)

        return Nota.objects.none()

class CarreraView(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer