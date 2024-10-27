import base64
from .models import piercings
from rest_framework import serializers
class PiercingsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    class Meta:
        model = piercings
        fields = ('name','description', 'price', 'photo')

    def get_imagen(self, obj):
        if obj.photo:
            return base64.b64encode(obj.photo).decode('utf-8')
        return None
