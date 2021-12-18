from rest_framework import serializers
from .models import AddBook , Comment, Rate, Favourite


class BookSerializer(serializers.ModelSerializer):
    
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
            'comments',
            'rate_count',
            'rate_value',
            'favourite',
            'favourite_count',
            
        )

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


class RateSerializer(serializers.ModelSerializer):

    book_rates_user = serializers.RelatedField(read_only=True)
    rates_book = serializers.RelatedField(read_only=True)

    class Meta:
        model = Rate
        fields = "__all__"

class FavouriteSerializer(serializers.ModelSerializer):

    #book_favourites_user = serializers.RelatedField(read_only=True)
    #favourites_book = serializers.RelatedField(read_only=True)
 
    class Meta:
        model = Favourite
        fields = "__all__"