from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')), 
    path('admin/', admin.site.urls),
    path('api/piercs/', include('piercings.urls')),
    path('api/tatts/', include('tattoos.urls')),
    path('keep_alive/', views.keep_alive, name='keep_alive'),
]
