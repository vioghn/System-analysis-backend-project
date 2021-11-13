from django.contrib import admin
from .models import AddBook

class AddBookAdmin(admin.ModelAdmin):
    list_display =  ( 
            'title', 
            'genre',
            'Description', 
            'bookAvatar', 
            'authors', 
            'publisher', 
            'publication_date', 
            )

admin.site.register(AddBook, AddBookAdmin)
