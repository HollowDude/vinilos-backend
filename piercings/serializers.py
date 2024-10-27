import base64
from .models import piercings
from rest_framework import serializers
class PiercingsSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    class Meta:
        model = piercings
        fields = '__all__'

    def get_imagen(self, obj):
        if obj.photos:
            return base64.b64encode(obj.photos).decode('utf-8')
        return None
