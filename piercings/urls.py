from django.urls import path, include
from rest_framework import routers
from .views import PiercingsViewSet

router = routers.DefaultRouter()
router.register(r'piercings', PiercingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]