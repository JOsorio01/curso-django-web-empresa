# Generated by Django 2.2 on 2019-05-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created_at'], 'verbose_name': 'Servicio'},
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='servicios', verbose_name='Imagen'),
        ),
    ]
