from rest_framework import serializers
from .models import AddBook


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddBook
        fields = ( 
            'id',
            'title', 
            'genre',
            'Description', 
            'bookAvatar', 
            'authors', 
            'publisher', 
            'publication_date', 
            )