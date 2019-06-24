from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Página'
        ordering = ['order', 'title']
