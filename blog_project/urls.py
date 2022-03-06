from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A web API for creaating and editing blog posts'
API_VERSION = 'v1'

schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version=API_VERSION,
        description=API_DESCRIPTION
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(
        title=API_TITLE, description=API_DESCRIPTION)
    ),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),

]
