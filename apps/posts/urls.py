from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import routing
from .views import (PostModelViewSetAPIView,
                    CategoryModelViewSetAPIView,
                    ThemeModelViewSetAPIView,
                    CommentModelViewSetAPIView)


router = SimpleRouter()
router.register(r'posts', PostModelViewSetAPIView, basename='posts-crud')
router.register(r'categories', CategoryModelViewSetAPIView, basename='category-crud')
router.register(r'themes', ThemeModelViewSetAPIView, basename='theme-crud')
router.register(r'comments', CommentModelViewSetAPIView, basename='comment-crud')

urlpatterns = router.urls + [
    path('', include(routing.websocket_urlpatterns)),
]
