from datetime import datetime
from django.db import models

def file_location(instance, filename, **kwargs):
    file_path = f"photo/{instance.title}-{filename}"
    return file_path

class tattoos(models.Model):
    name = models.CharField(max_length=255, default="No definido")
    description = models.CharField(max_length = 255, default="No hay descripcion")
    photo = models.ImageField(upload_to=file_location, null=False, blank=True)
    date = models.DateField(default = datetime.now())
    price = models.IntegerField(default=int(1))
