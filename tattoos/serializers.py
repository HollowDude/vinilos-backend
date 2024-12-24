import base64
from .models import tattoos
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class TattooSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)

    class Meta:
        model = tattoos
        fields = ('name','description', 'photo_b64', 'date', 'price')
