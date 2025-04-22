from .models import University, Faculty, Chair, Group, Student
from rest_framework import serializers


class UniversitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class FacultySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


