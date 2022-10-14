from .models import CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        data = super().validate(attrs)
        # print ("\n\n data - ", data, "\n\n")
        dictionary = dict(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        CustomUser.objects.filter(email = dictionary['email']).update(refreshtoken = data['refresh'])
        # print ("\n\n dictionary - ", dictionary, "\n\n")
        return data


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ('name', 'totmarks', 'city', 'email', 'password')

        extra_kwargs  = {
            "password": { 'write_only' : True}
        }
    
    def create(self, validated_data):

        Pass = validated_data.get('password')
        validated_data['password'] = make_password(Pass)
        return super(UserRegisterSerializer, self).create(validated_data)


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ('id', 'name', 'totmarks', 'city', 'email')
