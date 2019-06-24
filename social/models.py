from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave')
    name = models.CharField(max_length=200, verbose_name='Red Social')
    url = models.URLField(verbose_name='Enlace', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'enlace'
        ordering = ['name']
