from django.contrib import admin
from .models import Album, Artist, Song, Comment


admin.site.register([Album, Artist, Song, Comment])
