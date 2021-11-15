from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Book(models.Model):
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)



class AddBook(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, null=True)
    bookAvatar = models.FileField(upload_to="book/image")
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()