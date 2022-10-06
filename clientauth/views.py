from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
import mysql.connector
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from .models import Student
from .serializers import StudentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password

def dbconnection():
    db1 = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "whocares@MySQL98!",
        database = "db1"
    )
    return db1

def tokens_user(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    print ("\n\n", refresh, "\n", access, "\n\n")
    return { 'refresh': str(refresh), 'access': str(access) }

@csrf_exempt
@api_view(['POST'])
def register (request):
    db = dbconnection()
    mycursor = db.cursor()
    respond = request.POST
    requested = respond.dict()
    SName = requested['Name']
    STotmarks = requested['Totmarks']
    SCity = requested['City']
    SEmail = requested['Email']
    SPasswd = requested['Passwd']
    Pass = make_password(SPasswd)
    mycursor.execute("INSERT INTO Student (Name, Totmarks, City, Email, Passwd) VALUES (%s, %s, %s, %s, %s)", (SName, STotmarks, SCity, SEmail, Pass))
    # serial = StudentSerializer(data = request.data)
    print ("\n\n Request Data : ", request.data, "\n\n")
    # serial.is_valid(raise_exception = True)
    # serial.save()
    # if serializer.is_valid():
    #     serializer.save()
    # RfshTk = request['RefreshToken']
    db.commit()
    finallst = { "POST": "The below user has been inserted.", "Student Name": SName, "Total Marks": STotmarks, "City": SCity, "Email": SEmail }
    return JsonResponse ( finallst )

@permission_classes([IsAuthenticated])
@api_view()
@csrf_exempt

def login(requested):
    flag = 0
    # db = dbconnection()
    # mycursor = db.cursor()
    respond = requested.POST
    request = respond.dict()
    Email = request['Email']
    Pass = request['Passwd']
    # authorization = requested.headers["Authorization"]
    # print ("\n\n", authorization, "\n\n")
    mycursor.execute("SELECT * FROM Student")
    for i in mycursor:
        if ( i[5] ==  str(Email)):
            flag = 1
            rst = check_password(Pass, i[6])
            if (rst):
                result = {"Status": "Successfullly logged in!", "Student ID": i[0], "Student Name" : i[1], "Total Marks" : i[2], "City" : i[3], "Email" : i[5]}
                break
            else:
                result = {"Status": "Incorrect details. Please try again."}
        else:
            result = {"Error ": "Enter a valid ID number."}
    if (flag == 0):
        result = {"Status": "User not found!"}
    finallst = {"Retrieved data" : result }
    return JsonResponse( finallst )
