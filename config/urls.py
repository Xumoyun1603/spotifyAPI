from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Music Application REST API",
        default_version="v1",
        description="Swagger docs for REST API",
        contact=openapi.Contact(
            'Nurimov Xumoyun <tuit20192022@gmail.com>',
        ),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]
