from django.db import models


class Observation(models.Model):
    name = models.CharField(max_length = 20)
    transient_type = models.CharField(max_length = 200, default = 'OT')
    obs_or_lim = models.CharField(max_length = 1, default = 'l')
    DataTime = models.DateTimeField()
    Ra = models.FloatField(null=True)
    Dec = models.FloatField(null=True)
    max_limit = models.IntegerField(null=True)
    max_magnitude = models.IntegerField(null=True)
    lightcurve = models.CharField(max_length = 300, default = 'http://observ.pereplet.ru/')
    pictures = models.ImageField(default = 'http://observ.pereplet.ru/')
    telescope = models.CharField(max_length = 30, default = 'MASTER')
    publication = models.CharField(max_length = 300, default = 'http://observ.pereplet.ru/')
    if_we_first = models.BooleanField(default = None)
    time_from_notice = models.IntegerField(null=True)
    satellite = models.CharField(max_length = 30, default = 'MASTER')
    discoverer = models.CharField(max_length = 30, default = 'Lipunov V. M.')

class Person(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

