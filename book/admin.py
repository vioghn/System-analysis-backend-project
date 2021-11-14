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
    list_filter = ( 
            'genre', 
            'publication_date', 
            )
    search_fields = ( 
            'title',
            'authors',
            'publisher', 
            'Description', 
            )

admin.site.register(AddBook, AddBookAdmin)
