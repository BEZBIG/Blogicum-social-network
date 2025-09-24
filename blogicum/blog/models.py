from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField('Опубликовано', default=True, help_text='Снимите галочку, чтобы скрыть публикацию')
    created_at = models.DateTimeField('Добавлено',auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'Опубликовать'
        verbose_name_plural = 'Опубликовано'
        ordering = ['-created_at']

class Post(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Заголовок')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True,
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        verbose_name='Местоположение',
        null=True, blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        null=True,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
    
class Category(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL;'
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class Location(PublishedModel):
    name = models.CharField('Название места', max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
    
