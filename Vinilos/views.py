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

    print(USERNAME)
    print(PASSWORD)
    print(os.getenv('USERNAME'))
    print(os.getenv('PASSWORD'))

    if USERNAME == os.getenv('USERNAME') and PASSWORD == os.getenv('PASSWORD'):
        return JsonResponse({'Bacano': 'Te autenticaste bacano'}, status = status.HTTP_200_OK)
    return JsonResponse({'Uh, problema':'No introdujiste bien un dato bro'}, status = status.HTTP_401_UNAUTHORIZED)


