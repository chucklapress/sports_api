from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    position = models.CharField(max_length=5)
    birth_year = models.IntegerField()

