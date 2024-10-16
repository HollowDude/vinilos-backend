from .models import tattoos
from rest_framework import serializers
class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model = tattoos
        fields = '__all__'
