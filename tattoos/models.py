from datetime import datetime
from django.db import models

class tattoos(models.Model):
    name = models.CharField(max_length=255, default="No definido")
    description = models.CharField(max_length = 255, default="No hay descripcion")
    photo = models.TextField(default="No Photo availed")
    date = models.DateField(default = datetime.now())
    price = models.IntegerField(default=int(1))
    def __str__(self):
        return self.name
