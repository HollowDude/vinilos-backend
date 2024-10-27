import base64
from .models import piercings
from rest_framework import serializers
class PiercingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = piercings
        fields = '__all__'

    def get_imagen(self, obj):
        if obj.photo:
            return base64.b64encode(obj.photo).decode('utf-8')
        return None