from django.db import models
from PIL import Image


class AddBook(models.Model):
    title = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    bookAvatar = models.FileField(upload_to="book/image", blank=True)
    authors = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    publication_date = models.DateField(blank=True)
