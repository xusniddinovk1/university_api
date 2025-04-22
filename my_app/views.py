from rest_framework import viewsets
from .models import University, Faculty, Chair, Group, Student
from .serializers import *


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializers


