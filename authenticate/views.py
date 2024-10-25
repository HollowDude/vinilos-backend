from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
#from django.middleware.csrf import get_token
from rest_framework import status

class LoginView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Intentando autenticar: {username} con la contraseña proporcionada")

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"Usuario autenticado: {user.username}")
            # Generar tokens de acceso y refresh
            refresh = RefreshToken.for_user(user)

            # Crear la respuesta
            response = Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

            # Establecer el access_token en una cookie
            response.set_cookie(
                key='access_token',
                value=str(refresh.access_token),
                httponly=True,  # Evita acceso desde JavaScript
                secure=False,   # Debe ser True si usas HTTPS en producción
                samesite='Lax', # Ayuda a prevenir ataques CSRF
            )

            return response
        else:
            print(f"Falló la autenticación para {username}")
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        #Recupera el refresh de cookies 
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({'Candela': 'No refresh token'}, status=401)
        
        try:
            data ={'refresh': refresh_token}
            response = super().post(request, data, *args, **kwargs)

            #Almaceno el new token de acceso en las cookies
            acces_token = response.data['acces']
            response.set_cookie(
                key='acces_token',
                value=acces_token,
                httponly=True,
                secure=True,
                samesite='Lax',
            )
            return response
        
        except InvalidToken as e:
            return Response({'detail': str(e)}, status=401)