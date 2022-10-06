from django.db import models
from django.core import validators

class Student(models.Model):
    Student_ID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 40)
    Totmarks = models.IntegerField()
    City = models.CharField(max_length = 40)
    RefreshToken = models.CharField(max_length = 1500)
    Email = models.EmailField(max_length = 80, unique = True, validators=[validators.EmailValidator(message="Invalid Email")])
    Passwd = models.CharField(max_length = 40)

    USERNAME_FIELD = 'Email' 
    REQUIRED_FIELDS = ['Passwd']

    def __str__(self):
        return self.Email