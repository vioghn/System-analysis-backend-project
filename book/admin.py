from django.contrib import admin
from .models import AddBook , Comment

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

class Commentadmin(admin.ModelAdmin):
    list_display =  ( 
            'id', 'body', 'owner', 'post'

            
            )
   




admin.site.register(AddBook, AddBookAdmin)
admin.site.register(Comment , Commentadmin)
