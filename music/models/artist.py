from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField(blank=True, null=True)
