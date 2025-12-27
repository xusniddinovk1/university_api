from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    university = models.ForeignKey(University, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Chair(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    chair = models.ForeignKey(Chair, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
