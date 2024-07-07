from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    year_of_study = models.IntegerField()

    def __str__(self):
        return self.name
