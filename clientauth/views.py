#from sqlite3 import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import mysql.connector 
# from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth.hashers import make_password, check_password

@api_view()

def dbconnection():
    db1 = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "whocares@MySQL98!",
        database = "db1"
    )
    return db1

@csrf_exempt
def register (requested):
    db = dbconnection()
    mycursor = db.cursor()
    respond = requested.POST
    request = respond.dict()
    SName = request['Name']
    Total_Marks = request['Totmarks']
    City = request['City']
    Email = request['Email']
    Pass = request['Passwd']
    RfshTk = request['RefreshToken']
    Passwd = make_password(Pass)
    mycursor.execute("INSERT INTO Student (Name, Totmarks, City, RefreshToken, Email, Passwd) VALUES (%s, %s, %s, %s, %s, %s )", (SName, Total_Marks, City, RfshTk, Email, Passwd))
    #db.commit()
    finallst = { "POST": "The below data has been inserted.", "Student Name": SName, "Total Marks": Total_Marks, "Student Name": City, "Email": Email, "Passwd": Passwd }
    return JsonResponse( finallst )

@api_view()
@csrf_exempt
@permission_classes([IsAuthenticated])
def login(requested):
    
    flag = 0
    db = dbconnection()
    mycursor = db.cursor()
    respond = requested.POST
    request = respond.dict()
    Email = request['Email']
    Pass = request['Passwd']
    authorization = requested.headers["Authorization"]
    print ("\n\n", authorization, "\n\n")
    mycursor.execute("SELECT * FROM Student")
    if (Email):
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
