import base64
from .models import tattoos
from rest_framework import serializers
class TattooSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(write_only = True)

    class Meta:
        model = tattoos
        fields = ('name','description', 'photo', 'photo_b64', 'date', 'price')

    def create(self, validated_data):
        photo = validated_data.pop('photo')
        photo_b64 = base64.encode_base64(photo.read()).decode('utf-8')
        validated_data['photo_b64'] = photo_b64
        return photo_b64.objects.create(**validated_data)
