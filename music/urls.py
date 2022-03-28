from django.urls import path
from .views import SongsAPIView


urlpatterns = [
    path('songs/', SongsAPIView.as_view(), name='songs'),
]