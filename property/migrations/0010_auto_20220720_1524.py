# Generated by Django 2.2.28 on 2022-07-20 12:24

from django.db import migrations


def load_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    needed_values = Flat.objects.values_list('owner', 'owners_phonenumber', 'owner_normalized_phone')
    for values in needed_values:
        owner, phonenumber, normalized_phone = values
        Owner.objects.get_or_create(
            full_name=owner, owners_phonenumber=phonenumber, defaults={'owner_normalized_phone': normalized_phone},
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220720_1522'),
    ]

    operations = [
        migrations.RunPython(load_owners),
    ]