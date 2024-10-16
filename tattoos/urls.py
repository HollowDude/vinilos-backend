from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tattoos', views.TattoosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('', views.TattoosListView.as_view(), name=None),
    #path('create/', views.TattooCreateView.as_view(), name=None),
    #path('ver/<str:id>/', views.Prueba.as_view())
]