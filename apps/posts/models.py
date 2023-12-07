from django.db import models
from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(
        _('Название'),
        max_length=100
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Post(BaseModel):
    title = models.CharField(
        _('Название'),
        max_length=100,
    )
    description = models.TextField(
        _('Описание')
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_('Категория'),
        on_delete=models.CASCADE,

    )
    themes = models.ManyToManyField(
        'Theme',
        _('Темы')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Посты')
        verbose_name_plural = _('Посты')


class Theme(models.Model):
    title = models.CharField(
        _('Название'),
        max_length=100
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Тема')
        verbose_name_plural = _('Темы')


class Comment(BaseModel):
    text = models.CharField(
        _('Комментарий'),
        max_length=300
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('Пост'),
        related_name='comments'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
