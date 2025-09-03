from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'Опубликовать'
        verbose_name_plural = 'Опубликовано'
        ordering = ['-created_at']

class Post(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Содержание')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
    
class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class Location(PublishedModel):
    name = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name
    
