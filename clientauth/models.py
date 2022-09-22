from sqlite3 import IntegrityError
from django.db import models

class Student(models.Model):
    Student_ID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length= 40)
    Totmarks = models.IntegerField()
    City = models.CharField(max_length= 40)
    try:
        RefreshToken = models.CharField(max_length= 1500)
        Email = models.CharField(max_length= 80, unique = True)
    except IntegrityError:
        lst = {"Error": "Email is already registered. Please try with a different email."}
    Passwd = models.CharField(max_length= 40)
