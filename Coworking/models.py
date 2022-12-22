from django.db import models
from datetime import datetime

# Create your models here.
class Coworking(models.Model):
    name = models.CharField(max_length=255)
    places_number = models.IntegerField()

    objects = models.Manager()

    class Meta:
        db_table = 'coworking'


class OccupiedSpaceInfo(models.Model):
    coworking = models.ForeignKey(to=Coworking, on_delete=models.CASCADE)
    places_occupied = models.IntegerField()
    time = models.DateTimeField(default=datetime.now())

    objects = models.Manager()

    class Meta:
        db_table = 'occupied_space'


class Rate(models.Model):
    coworking = models.ForeignKey(Coworking, on_delete=models.CASCADE)
    mark = models.IntegerField()

    objects = models.Manager()

    class Meta:
        db_table = 'rate'
