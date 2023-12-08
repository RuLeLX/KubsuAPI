from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from Account.models import *
from .serializers import *
from Account.serializers import *
import jwt
import re #Check login 

@api_view(['POST'])  #Auth user in system
def AuthUser(request):

    #Who is have login? Student, Teacher or Decan
    def check_login_student(login): #for student this is id
        check_login = re.match(r's\d{7}', login)

        if check_login == None or login != check_login.group():
            return False
        return True
    
    def check_login_teacher(email): #email

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        if re.match(pattern, email):
            return True
        return False
    
    def check_login_decan(login):
        #For decans special login in database
        pass

    login = request.data['login']
    password = request.data['password']

    if check_login_student(login):
        datauser = StudentSerializer(Students.objects.filter(id_students=login, password=password))

    
    #return Response(datauser)

