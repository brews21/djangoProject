from django.db import models

# Create your models here.

class Topic(models.Model):
    """docstring for Topic."""
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    """docstring for Webpage."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    """docstring for AccessRecord."""
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    """docstring for User."""
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.first_name + self.last_name
