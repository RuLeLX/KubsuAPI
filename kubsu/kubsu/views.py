from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from Account.models import *
from .serializers import *
import jwt
import re #Check login 

@api_view(['POST'])  #Auth user in system
def AuthUser(request):
    #Who is have login? Student, Teacher or Decan
    login = request.data['login']
    password = request.data['password']

    

    datauser = {
        "login": login,
        "password": password
    }
    return Response(datauser)

