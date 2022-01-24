from django.contrib import admin

from book.views import read, savebook
from .models import AddBook , Comment, Rate, Favourite , Reply , notification , Read , Saved

class AddBookAdmin(admin.ModelAdmin):
    list_display =  ( 
            'title', 
            'genre',
            'Description', 
            'bookAvatar', 
            'authors', 
            'publisher', 
            'publication_date', 
            'comments',
            'rate_count',
            'rate_value',
            'favourite',
            'favourite_count',
            
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
   

admin.site.register(notification)
admin.site.register(Read)
admin.site.register(Saved)
admin.site.register(Favourite)
admin.site.register(Rate)
admin.site.register(Reply)
admin.site.register(AddBook, AddBookAdmin)
admin.site.register(Comment , Commentadmin)

