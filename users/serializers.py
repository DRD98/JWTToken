from .models import CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('name', 'totmarks', 'city', 'email', 'password')

        extra_kwargs  = {
            "password": { 'write_only' : True}
        }
    
    def create(self, validated_data):
        # MailID = validated_data.get('MailID')
        Pass = validated_data.get('password')
        validated_data['password'] = make_password(Pass)
        return super(UserRegisterSerializer, self).create(validated_data)
