from django.db import models

# Create your models here.


class Starship(models.Model):
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=100)
    ship_class = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)

    def __str__(self):
        return self.name