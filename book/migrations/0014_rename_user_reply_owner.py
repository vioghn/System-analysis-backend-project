# Generated by Django 3.2.10 on 2022-01-21 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20220121_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='user',
            new_name='owner',
        ),
    ]
