from django.db import models


class Song(models.Model):
    album = models.ForeignKey('music.Album', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    cover = models.URLField(blank=True, null=True)
    source = models.URLField()

    def __str__(self):
        return self.title

