from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    cover = models.URLField(blank=True, null=True)
    source = models.URLField()