from rest_framework.viewsets import ModelViewSet
from .models import Post, Category, Comment, Theme
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, ThemeSerializer, PostValidateSerializer
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class PostModelViewSetAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = PostValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        themes = request.data.get('themes')

        post = Post.objects.create(
            title=serializer.validated_data.get('title'),
            description=serializer.validated_data.get('description'),
            category_id=serializer.validated_data.get('category'),
        )

        post.themes.set(themes)
        post.save()

        return Response(data={'message': 'Data received!',
                              'movie': self.get_serializer(post).data},
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'post_group',
            {
                'type': 'notify.post.published',
                'message': 'Ваш пост опубликован',
            }
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryModelViewSetAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ThemeModelViewSetAPIView(ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    lookup_field = 'id'


class CommentModelViewSetAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
