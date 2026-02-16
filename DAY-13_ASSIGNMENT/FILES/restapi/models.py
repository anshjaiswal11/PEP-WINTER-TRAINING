from django.db import models

# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    published_date = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name