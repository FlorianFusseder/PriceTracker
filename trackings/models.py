from django.db import models


class Tracking(models.Model):
    url = models.CharField(max_length=100)
