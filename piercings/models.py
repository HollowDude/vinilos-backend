from django.db import models


class piercings(models.Model) :
    name = models.CharField(max_length = 255, default = "No name")
    description = models.CharField(max_length = 255, default = "No description")
    price = models.IntegerField(default = int(1))
    photo = models.BinaryField()
    def __str__(self):
        return self.name