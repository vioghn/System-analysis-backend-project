# Generated by Django 4.0 on 2021-12-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_remove_favourite_favourite_addbook_favourite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='favourite_count',
            field=models.IntegerField(default=1),
        ),
    ]
