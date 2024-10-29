from .models import piercings
from .serializers import PiercingsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

class PiercingsViewSet(viewsets.ModelViewSet) :
    queryset = piercings.objects.all()
    serializer_class = PiercingsSerializer

    def get_permissions(self):
        if self.action in ['list','retrive']:
            return [AllowAny()]
        return [IsAuthenticated()]
    