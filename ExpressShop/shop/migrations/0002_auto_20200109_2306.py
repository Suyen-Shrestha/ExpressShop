# Generated by Django 2.2.9 on 2020-01-09 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='type',
            new_name='address_type',
        ),
    ]