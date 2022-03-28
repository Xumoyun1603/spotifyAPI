from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    cover = models.URLField(blank=True, null=True)

