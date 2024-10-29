from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import os

def keep_alive(request):
    return JsonResponse({'status': 'active'})



@api_view(['POST'])
def is_auth(request):
    username = request.data.get('user')
    password = request.data.get('pass')

    if username == os.getenv('USERNAME') and password == os.getenv('PASSWORD'):
        return JsonResponse({'Bacano': 'Te autenticaste bacano'}, 200)
    return JsonResponse({'Uh, problema':'No introdujiste bien un dato bro'}, status = status.HTTP_401_UNAUTHORIZED)

