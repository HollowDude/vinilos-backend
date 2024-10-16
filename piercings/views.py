from .models import piercings
from .serializers import PiercingsSerializer
from rest_framework import viewsets

class PiercingsViewSet(viewsets.ModelViewSet) :
    queryset = piercings.objects.all()
    serializer_class = PiercingsSerializer