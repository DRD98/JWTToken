from django.shortcuts import render
from .models import StudModel
from .serializers import StudentViewSerializer, StudentRegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

# @api_view(['GET'])
# def StudentView(request):
#     obj = request.objects.all()
#     serializer = StudentViewSerializer(obj, many = True)
#     return Response(serializer.data)

@api_view(['POST'])
def StudentRegisterView(request):
    serializer = StudentRegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        # print ("\n\n Passwd - ", serializer.data['Passwd'], "\n\n")
        return JsonResponse({"Status":"User successfully registered!", "Data : " : serializer.data}, status = 201)
    return JsonResponse(serializer.errors, status = 400)  

@api_view(['POST'])
def StudentLoginView(requested):
    respond = requested.POST
    request = respond.dict()
    mail = request['MailID']
    passd = request['password']
    user = StudModel.objects.get(MailID = mail)
    # serializer = StudentRegisterSerializer(data = request.data)
    print ("\n\n User - ", user, "\n\n")
    if user is None:
        raise AuthenticationFailed('User not found! Please try with another email ID.')    
    if not user.check_password(passd):
        print ("\n\n Password - ", passd, "\n\n")
        raise AuthenticationFailed('Incorrect password.')
    print ("\n\n User - ", mail, "\n\n")
    res = {"mail": "user"}
    return Response( res )

# FOLLOWING NOT NEEDED

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['name'] = user.name
#         # ...

#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer