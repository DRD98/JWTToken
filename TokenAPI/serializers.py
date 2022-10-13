from rest_framework import serializers,validators
from .models import StudModel
from django.contrib.auth.hashers import make_password

class StudentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudModel
        fields = '__all__'

# class StudentLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudModel
#         fields = ('MailID', 'Passwd')
#         MailID = validated_data.get('MailID')
#         Pass = validated_data.get('Passwd')

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudModel
        fields = ('Student_ID', 'Name', 'Totmarks', 'City', 'MailID', 'Passwd')        

        extra_kwargs  = {
            "password":{'write_only':True},
            "email":{'required':True,
            "allow_blank":False,
            "email": {"validators": [validators.UniqueValidator(StudModel.objects.all(),"User with this email already exist. Try another mail ID!")]}
            } 
            }

    def create(self, validated_data):
        # Name = validated_data.get('Name')
        # Totmarks = validated_data.get('Totmarks')
        # City = validated_data.get('City')
        MailID = validated_data.get('MailID')
        # validated_data['Passwd'] = make_password(validated_data.get('Passwd'))
        Pass = validated_data.get('Passwd')
        # print ("\n\n Pass - ", Pass, "\n\n")
        # print ("\n\n Validated Data - ", validated_data['Passwd'], "\n\n")
        # Passwd = make_password(Pass)
        validated_data['Passwd'] = make_password(Pass)
        # print ("\n\n Hashed Validated Data - ", validated_data['Passwd'], "\n\n")
        return super(StudentRegisterSerializer, self).create(validated_data)   