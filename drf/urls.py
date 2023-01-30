from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from app.views import AuthorModelViewSet, ArticleModelViewSet, BiographyModelViewSet, BookModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('book', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('article', ArticleModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
]
