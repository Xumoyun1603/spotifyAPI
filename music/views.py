from rest_framework.views import APIView
from rest_framework.response import Response

from music.models import Song
from music.serializers import SongSerializer


class SongsAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(True)

        serializer.save()

        return Response(data=serializer.data)