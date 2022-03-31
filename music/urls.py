from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import (
    SongViewSet, AlbumViewSet, ArtistViewSet,
    CommentAPIView, CommentDetailAPIView
)

router = DefaultRouter()
router.register('songs', SongViewSet, "songs")
router.register('albums', AlbumViewSet, "albums")
router.register('artists', ArtistViewSet, "artists")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('songs/<int:pk>/comments/', CommentAPIView.as_view(), name='comments'),
    path('songs/<int:pk>/comments/<int:pk_alt>/', CommentDetailAPIView.as_view(), name='comment'),
]