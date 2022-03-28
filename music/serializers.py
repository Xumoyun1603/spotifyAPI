from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from music.models import Song, Album, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    # artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer()

    class Meta:
        model = Song
        fields = ('id', 'album', 'title', 'cover', 'source', 'listened')

    def validate_source(self, value):

        if not value.endswith('.mp3'):
            raise ValidationError(detail='Mp3 file is required')

        return value
