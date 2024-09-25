from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
