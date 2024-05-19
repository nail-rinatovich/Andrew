from django.db import models
from django.urls import reverse # Новый импорт
import datetime
from mptt.models import MPTTModel, TreeForeignKey
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория', blank=True, null=True) 
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title