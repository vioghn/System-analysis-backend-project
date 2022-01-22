from rest_framework import serializers

from .models import AddBook , Comment, Rate, Favourite , Reply , notification , Read, Saved
from django.db.models import Sum




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



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reply = serializers.PrimaryKeyRelatedField(many=True, read_only=True )
   
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post' , 'reply']
    
    # def get_replies(self, obj):
    #     if obj.is_parent:
    #         return CommentchildSerializer(obj.children(), many=True).data
    #     return None

    # def get_reply_count(self, obj):
    #     if obj.is_parent:
    #         return obj.children().count()
    #     return 0


# class CommentchildSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
   
#     class Meta:
#         model = Comment
#         fields = ['id', 'body', 'owner', 'post']

class ReplySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Reply
        fields = ['id' , 'owner','body' , 'comment' ]


class notifserializer(serializers.ModelSerializer):
      class Meta:
        model = notification
        fields = ['id' , 'user','body'  ]


class SavedSerializer(serializers.ModelSerializer):

    book_saved_user = serializers.RelatedField(read_only=True)
    saved_book = serializers.RelatedField(read_only=True)
 
    class Meta:
        model = Saved
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):

    book_read_user = serializers.RelatedField(read_only=True)
    read_book = serializers.RelatedField(read_only=True)
 
    class Meta:
        model = Read
        fields = "__all__"
