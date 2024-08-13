from django.db import models


class Observation(models.Model):
    transient_type = models.CharField()
    obs_or_lim = models.BooleanField()
    DataTime = models.DateTimeField()
    coordinates = models.CharField()
    max_limit = models.IntegerField()
    max_magnitude = models.IntegerField()
    lightcurve = models.CharField()
    pictures = models.ImageField()
    telescope = models.CharField()
    publication = models.CharField()
    if_we_first = models.BooleanField()
    time_from_notice = models.IntegerField()

