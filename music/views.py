from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import filters

from django.db import transaction
from django.shortcuts import get_object_or_404

from music.models import Song, Album, Artist, Comment
from music.serializers import (
    SongSerializer, AlbumSerializer, ArtistSerializer, CommentSerializer
)


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("listened", "-listened")
    # search_fields = ("title", "album__artist__name", "album__title")

    def get_queryset(self):
        queryset = Song.objects.all()
        query = self.request.query_params.get('search')

        if (query is not None) and query != '':
            queryset = Song.objects.annotate(
                similarity=Greatest(
                    TrigramSimilarity('title', query),
                    TrigramSimilarity('album__artist__name', query),
                )
            ).filter(similarity__gt=0.4).order_by('-similarity')

        return queryset

    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with transaction.atomic():
            song.listened += 1
            song.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:10]
        serializer = SongSerializer(songs, many=True)

        return Response(data=serializer.data)


class CommentAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        song = get_object_or_404(Song, pk=pk)

        comments = song.comments.all()

        serializer = CommentSerializer(comments, many=True)

        return Response(data=serializer.data)

    def post(self, request, pk=None):
        song = get_object_or_404(Song, pk=pk)

        request.data['user_id'] = request.user.id
        request.data['song_id'] = song.id

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            comment = Comment(
                song_id=data['song_id'],
                user_id=data['user_id'],
                text=data['text'],
            )
            comment.save()
            song.comments.add(comment)

            return Response({'status': 'The comment successfully created'})

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, pk_alt=None):
        song = get_object_or_404(Song, pk=pk)
        comment = get_object_or_404(song.comments, pk=pk_alt)

        serializer = CommentSerializer(comment)

        return Response(data=serializer.data)

    def delete(self, request, pk=None, pk_alt=None):
        song = get_object_or_404(Song, pk=pk)
        comment = get_object_or_404(song.comments, pk=pk_alt)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)

        return Response(data=serializer.data)

