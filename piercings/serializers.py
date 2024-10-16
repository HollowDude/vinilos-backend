from .models import piercings
from rest_framework import serializers
class PiercingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = piercings
        fields = '__all__'
