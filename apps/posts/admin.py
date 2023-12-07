from django.contrib import admin
from .models import Post, Category, Theme, Comment


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', )
    search_fields = ('text', )

