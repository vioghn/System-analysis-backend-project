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
    favourite = models.BooleanField(default=False, blank=True, null=True)
    favourite_count = models.IntegerField(default=0)

    @property
    def rate_count(self):
        return Rate.objects.filter(book_id=self.id).count()

    @property
    def rate_value(self):
        if Rate.objects.filter(book_id=self.id).count() is 0:
            return 0
        return Rate.objects.filter(book_id=self.id).aggregate(Avg('rate'))['rate__avg']


class Rate(models.Model):

    user = models.ForeignKey('account.Account', related_name='book_rates_user', on_delete=models.CASCADE, blank=True)
    book = models.ForeignKey('book.AddBook', related_name='rates_book', on_delete=models.CASCADE, blank=True)
    rate = models.IntegerField(default=2, blank=True, null=True)

    def str(self):
        return self.book

class Favourite(models.Model):

    user = models.ForeignKey('account.Account', related_name='book_favourites_user', on_delete=models.CASCADE, blank=True)
    book = models.ForeignKey('book.AddBook', related_name='favourites_book', on_delete=models.CASCADE, blank=True)

    def str(self):
        return self.book


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('account.Account', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('book.AddBook', related_name='comments', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    class Meta:
        ordering = ['created']

    # def children(self):
    #     return Comment.objects.filter(parent=self)

    # @property
    # def is_parent(self):
    #     if self.parent is not None:
    #         return False
    #     return True

  

class notification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    user = models.ForeignKey('account.Account', related_name='notif', on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['created']


class Reply(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('account.Account', related_name='reply', on_delete=models.CASCADE, blank=True)
    comment = models.ForeignKey('book.Comment', related_name='reply', on_delete=models.CASCADE, blank=True)
    isread  = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']


class Saved(models.Model):

    user = models.ForeignKey('account.Account', related_name='book_saved_user', on_delete=models.CASCADE, blank=True)
    book = models.ForeignKey('book.AddBook', related_name='saved_book', on_delete=models.CASCADE, blank=True)
    saved = models.BooleanField(default=False, blank=True, null=True)
    
    def str(self):
        return self.book

class Read(models.Model):

    user = models.ForeignKey('account.Account', related_name='book_read_user', on_delete=models.CASCADE, blank=True)
    book = models.ForeignKey('book.AddBook', related_name='read_book', on_delete=models.CASCADE, blank=True)
    read = models.BooleanField(default=False, blank=True, null=True)
    
    def str(self):
        return self.book
