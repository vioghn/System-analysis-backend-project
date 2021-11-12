from rest_framework import serializers
from .models import AddBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBook
        fields = (
            'selectedTopic', 
            'title', 
            'Description', 
            'bookAvatar', 
            'authors', 
            'publisher', 
            'publication_date', 
            )