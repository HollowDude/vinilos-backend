##from django.shortcuts import render
from .models import tattoos
from . import serializers
from rest_framework import viewsets


class TattoosViewSet(viewsets.ModelViewSet):
    queryset = tattoos.objects.all()
    serializer_class = serializers.TattooSerializer
