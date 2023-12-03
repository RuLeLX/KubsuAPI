from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
import jwt

@api_view(['POST'])  #Auth user in system
def AuthUser(request):

    response = {
        'name': request.data['name'],
        'surname': request.data['surname'],
    }

    return Response(response)