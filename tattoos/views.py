##from django.shortcuts import render
from .models import tattoos
from . import serializers
from rest_framework import viewsets


class TattoosViewSet(viewsets.ModelViewSet):
    queryset = tattoos.objects.all()
    serializer_class = serializers.TattooSerializer

"""
#Otras ways:

class TattoosListView(generics.ListAPIView):
    queryset = tattoos.objects.all()
    serializer_class = serializers.TattooSerializer


class TattooCreateView(generics.CreateAPIView):
    queryset = tattoos.objects.all()
    serializer_class = serializers.TattooSerializer
    def create(self, request, *args, **kwargs):
        super(TattooCreateView, self).create(request, args, kwargs)
        response = {"statusc_code": status.HTTP_200_OK,
                    "message": "Se creo bien",
                    "tallas:": request.data}
        return Response(response) 

        
#To esto es para lo de serializar y desserializar:

class Prueba(APIView):
    def get(self, request, id):
        qs = tattoos.objects.get(id = id)
        print(qs.name)
        hola = serializers.TattooSerializer(qs)
        return Response({
            "a":  hola.data
        })
"""