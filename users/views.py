from .serializers import UserLoginSerializer, UserRegisterSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomerLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class UserRegisterView(APIView):

    def post(self, request):
        
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print ()
            return JsonResponse({"Status":"User successfully registered!", "Data : " : serializer.data}, status = 201)
        return JsonResponse(serializer.errors, status = 400)  

