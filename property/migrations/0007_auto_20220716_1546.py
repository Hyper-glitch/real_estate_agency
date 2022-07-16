# Generated by Django 2.2.24 on 2022-07-16 12:46

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_complaint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AddField(
            model_name='flat',
            name='owner_normalized_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]