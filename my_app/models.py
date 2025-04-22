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
