# Generated by Django 3.2.9 on 2021-12-12 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0003_merge_0002_auto_20211126_0126_0002_auto_20211202_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, default=2, null=True)),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rates_book', to='book.addbook')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_rates_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
