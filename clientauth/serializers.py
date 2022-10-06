from msvcrt import kbhit
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # class Meta:
    model = Student
    # date_joined = None
    fields = ["Name", "Totmarks", "City", "Email", "Passwd"]