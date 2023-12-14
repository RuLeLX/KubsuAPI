from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from Account.models import *
from .serializers import *
from Account.serializers import *
import jwt
import re #Check login 
from .AbstractUser import *

@api_view(['POST'])  #Auth user in system
def AuthUser(request):

    login = request.data['login']
    password = request.data['password']

    datauser = UserSystem(login, password).get()

    return Response(datauser.data)

