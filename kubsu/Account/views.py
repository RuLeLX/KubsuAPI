from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
import jwt
from .serializers import *

@api_view(['POST'])
def UserData(request):
    usertoken = request.data['jwt']
    data = jwt.decode(usertoken, 'secret', algorithm='HS256') #dictionary

    
    

    return Response(data)