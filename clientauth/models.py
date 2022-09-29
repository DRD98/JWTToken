from django.db import models
# from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    username = None
    Student_ID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length= 40)
    Totmarks = models.IntegerField()
    City = models.CharField(max_length= 40)
    RefreshToken = models.CharField(max_length= 1500)
    Email = models.EmailField(max_length= 80, unique = True)
    Passwd = models.CharField(max_length= 40)
    USERNAME_FIELD = 'Email' 
    REQUIRED_FIELDS = [Email]

    def __str__(self):
        return self.Email