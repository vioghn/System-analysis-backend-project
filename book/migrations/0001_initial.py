# Generated by Django 3.2.8 on 2021-11-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100, null=True)),
                ('bookAvatar', models.FileField(upload_to='book/image')),
                ('authors', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
            ],
        ),
    ]
