from rest_framework import viewsets
from .serializers import *


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializers


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = UniversitySerializers


class ChairViewSet(viewsets.ModelViewSet):
    queryset = Chair.objects.all()
    serializer_class = UniversitySerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = UniversitySerializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = UniversitySerializers
