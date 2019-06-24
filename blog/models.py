from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Categoría')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Categoria'
        ordering = ['-created_at']


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=timezone.now)
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Entrada'
        ordering = ['-created_at']