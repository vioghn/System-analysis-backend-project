from rest_framework import serializers
from .models import AddBook , Comment, Rate


class BookSerializer(serializers.ModelSerializer):
    #rate_count = serializers.ReadOnlyField()
    #rate_value = serializers.ReadOnlyField()
    
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
            'comments'
            
        )

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


class RateSerializer(serializers.ModelSerializer):

    book_rates_user = serializers.RelatedField(read_only=True)
    rates_book = serializers.RelatedField(read_only=True)
    #user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rate
        fields = ['id','user','book','rate', 'rates_book', 'book_rates_user']