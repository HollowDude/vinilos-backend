from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')), 
    path('admin/', admin.site.urls),
    path('api/piercs/', include('piercings.urls')),
    path('api/tatts/', include('tattoos.urls'))
]