import base64
from .models import piercings
from rest_framework import serializers
class TattooSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    class Meta:
        model = tattoos
        fields = ('name','description', 'photo', 'date', 'price')

    def get_imagen(self, obj):
        if obj.photo:
            return base64.b64encode(obj.photo).decode('utf-8')
        return None
