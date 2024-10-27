from .models import tattoos
from rest_framework import serializers
import base64

class TattooSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    class Meta:
        model = tattoos
        fields = '__all__'

    def get_imagen(self, obj):
            if obj.photo:
                return base64.b64encode(obj.photo).decode('utf-8')
            return None
