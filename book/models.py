from django.db import models
from PIL import Image
from django.db.models import Avg



class AddBook(models.Model):
    title = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    bookAvatar = models.FileField(upload_to="book/image", blank=True)
    authors = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)

    publication_date = models.DateField(blank=True)






class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('account.Account', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('book.AddBook', related_name='comments', on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['created']



