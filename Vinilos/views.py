from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import os

def keep_alive(request):
    return JsonResponse({'status': 'active'})




@api_view(['POST'])
def is_auth(request):
    USERNAME = request.data.get('username')
    PASSWORD = request.data.get('password')

    if USERNAME == os.getenv('USERNAME') and PASSWORD == os.getenv('PASSWORD'):
        return JsonResponse({'Bacano': 'Te autenticaste bacano'}, 200)
    return JsonResponse({'Uh, problema':'No introdujiste bien un dato bro'}, status = status.HTTP_401_UNAUTHORIZED)


