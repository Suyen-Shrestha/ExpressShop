# Generated by Django 2.2.9 on 2020-01-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
            ],
        ),
    ]
