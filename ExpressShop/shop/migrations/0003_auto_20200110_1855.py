# Generated by Django 2.2.9 on 2020-01-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200109_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('shirt', 'Shirt'), ('sport wear', 'Sport wear'), ('out wear', 'Outwear')], max_length=70),
        ),
    ]