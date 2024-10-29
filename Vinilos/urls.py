from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/piercs/', include('piercings.urls')),
    path('api/tatts/', include('tattoos.urls')),
    path('keep_alive/', views.keep_alive, name='keep_alive'),
    path('auth/', views.is_auth, name='auth'),
]
