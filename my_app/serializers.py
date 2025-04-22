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


class ChairSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
