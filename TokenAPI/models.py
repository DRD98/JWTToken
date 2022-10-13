from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser


# class StudModel(AbstractUser):

    # username = None
    # Student_ID = models.AutoField(primary_key = True)
    # Name = models.CharField(max_length = 150)
    # Totmarks = models.IntegerField()
    # Mail = models.CharField(max_length = 40)
    # City = models.CharField(max_length = 40)
    # RefreshToken = models.CharField(max_length = 1000)
    # MailID = models.EmailField(max_length = 80, unique = True, validators=[validators.EmailValidator(message="Invalid Email")] )
    # Passwd = models.CharField(max_length = 1500)

#     class Meta:
#         db_table = 'students'

#     USERNAME_FIELD = 'MailID'
#     REQUIRED_FIELDS =  []

#     def __str__(self):
#         return self.Name
