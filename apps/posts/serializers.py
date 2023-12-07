from rest_framework import serializers
from .models import Post, Category, Comment, Theme


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    themes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'category', 'themes', 'comments')

    def get_category(self, posts):
        return posts.category.title

    def get_themes(self, posts):
        themes = [theme.title for theme in posts.themes.all()]
        return themes


class PostValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=30)
    description = serializers.CharField(min_length=5, max_length=500)
    category = serializers.IntegerField()
    themes = serializers.ListField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

