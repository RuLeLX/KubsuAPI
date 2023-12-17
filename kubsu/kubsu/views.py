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


    #Create jwt auth
    payload = datauser.data
    if payload == Error.data:
        return Response(Error.data)

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response

    #return Response(payload)

