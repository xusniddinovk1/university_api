from .models import University, Faculty, Chair, Group, Student
from rest_framework import serializers


class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ChairSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
