from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class UniversityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = University.objects.all()
    serializer_class = UniversitySerializers


class FacultyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers


class ChairViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chair.objects.all()
    serializer_class = ChairSerializers


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
