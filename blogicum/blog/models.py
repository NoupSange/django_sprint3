from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
chars = 256

class CommonDataAbstractModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True


class Post(CommonDataAbstractModel):
    title = models.CharField(max_length=chars, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем '
                   '— можно делать отложенные публикации.')
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        verbose_name='Местоположение',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        null=True,
    )

    class Meta():
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title[:15]


class Category(CommonDataAbstractModel):
    title = models.CharField(max_length=chars, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.')
    )

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:15]


class Location(CommonDataAbstractModel):
    name = models.CharField(max_length=chars, verbose_name='Название места')

    class Meta():
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:15]
