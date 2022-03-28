from django.urls import path
from .views import HelloWorldAPIView


urlpatterns = [
    path('hello-world/', HelloWorldAPIView.as_view(), name='hello-world'),
]