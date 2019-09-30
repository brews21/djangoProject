from django.db import models

# Create your models here.

class School(models.Model):
    name = models.TextField()
    principle = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.TextField()
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
