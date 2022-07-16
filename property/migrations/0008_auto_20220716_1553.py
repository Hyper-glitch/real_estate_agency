# Generated by Django 2.2.24 on 2022-07-16 12:53
import phonenumbers
from django.db import migrations


def normalize_owner_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    region = 'RU'
    owner_phonenumbers = Flat.objects.values_list('pk', 'owners_phonenumber')
    for values in owner_phonenumbers:
        pk = values[0]
        number = values[1]
        phonenumber = phonenumbers.parse(number, region)

        if phonenumbers.is_valid_number(phonenumber):
            normalized_phone = f'+{phonenumber.country_code}{phonenumber.national_number}'
            Flat.objects.filter(pk=pk).update(owner_normalized_phone=normalized_phone)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_auto_20220716_1546'),
    ]

    operations = [
        migrations.RunPython(normalize_owner_phonenumber),
    ]
