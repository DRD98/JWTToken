import jwt
from Token.settings import SECRET_KEY
from .models import CustomUser
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserDetailSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = UserLoginSerializer
    # print ("\n\n serializer_class = ", serializer_class, "\n\n")

    # def post(self, request):

        # serializer_class = UserLoginSerializer
        # token_obtain_pair = TokenObtainPairView.as_view()
        # respond = request.POST
        # response = respond.dict()
        # user = authenticate(request, email = response['email'], password = response['password'])
        # print ("\n\n token_obtain_pair = ", token_obtain_pair.data, "\n\n")
        # if user is not None:
        #     return JsonResponse({"Status " : " User login successful!"}, status = 201)
        # else:
        #     return JsonResponse({"Status " : " User login unsuccessful! Please try again."}, status = 400)


class UserRegisterView(APIView):

    def post(self, request):
        
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Status ":" User successfully registered!", "Data : " : serializer.data}, status = 201)
        return JsonResponse(serializer.errors, status = 400)  


class UserProfileView(APIView):
    authenticaton_classes = ( JWTAuthentication, )
    permission_classes = ( IsAuthenticated, )

    def get(self, request):
        txt = request.headers['Authorization']
        temp = txt.split()
        token = temp[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms = ['HS256'])
        print ("\n\n payload = ", payload['user_id'], "\n\n")
        student = CustomUser.objects.get(id = payload['user_id'])
        serializer = UserDetailSerializer(student, many = False)
        print ("\n\n Serializer Data = ", serializer.data, "\n\n")
        return JsonResponse (serializer.data)