# Generated by Django 2.2.24 on 2022-07-16 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20220714_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто поставил лайк'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='is_building_new',
            field=models.BooleanField(choices=[(True, 'Да'), (False, 'Нет'), (None, 'Неизвестно')], default=None, null=True, verbose_name='Новостройка'),
        ),
    ]
