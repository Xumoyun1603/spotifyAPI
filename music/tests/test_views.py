from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from music.models import Artist, Album, Song


class TestArtistViewSet(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            'john', 'john01@gmail.com', 'john12345$'
        )

        self.token = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()

        self.artist = Artist.objects.create(name="Example Artist")

    def test_get_all_albums(self):
        token = self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token[0]}")
        response = self.client.get("/artists/", token)
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Example Artist')


class TestSongViewSet(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            'john', 'john01@gmail.com', 'john12345$'
        )

        self.token = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()

        self.artist = Artist.objects.create(name="Test Artist")
        self.album = Album.objects.create(artist=self.artist, title="Test Album")
        self.song = Song.objects.create(album=self.album, title='Test Song')

    def test_search(self):
        token = self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token[0]}")
        response = self.client.get('/songs/?search=Test', token)
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['title'], 'Test Song')

