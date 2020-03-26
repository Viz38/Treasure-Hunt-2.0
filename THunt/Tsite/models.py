from django.db import models

# Create your models here.


class Student(models.Model):

    p = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    usn = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    branch = models.CharField(max_length=3)

    def __str__(self):
        return self.name
