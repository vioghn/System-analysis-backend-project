from rest_framework import serializers
from .models import AddBook , Comment 
from django.db.models import Sum




class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddBook

       

        comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True )
       
        fields = (
            'pk',
            'title', 
            'genre',
            'Description', 
            'bookAvatar', 
            'authors', 
            'publisher', 
            'publication_date', 
            'comments' , 
        
            
            
            
            
        )

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


