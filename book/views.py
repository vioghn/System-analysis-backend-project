from email.quoprimime import body_check
from os import access
from rest_framework.decorators import api_view, permission_classes, authentication_classes 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from datetime import date, timedelta
from rest_framework.views import APIView 
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .utils import Util
from django.http import Http404, request
from .models import AddBook  , Comment, Favourite  , Rate , Reply, notification , Read , Saved
from .serializers import BookSerializer , CommentSerializer, RateSerializer, FavouriteSerializer , ReplySerializer, notifserializer , ReadSerializer , SavedSerializer
from rest_framework import filters,generics,status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from book.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def add_book(request):
    data = dict(request.POST)
    print(data)
    addbook = AddBook.objects.filter(title=data['title'][0])
    if list(addbook) != []:
        return Response({'message': 'book has added'})
    addbook = AddBook.objects.create(      
        title=data['title'][0],
        genre=data['genre'][0],
        authors=data['authors'][0],
        publication_date=data['publication_date'][0],
    )
    addbook.save()
    if "Description" in request.data.keys() :
        addbook.Description=data['Description'][0]
    addbook.save()
    if "publisher" in request.data.keys() :
        addbook.publisher=data['publisher'][0]
    addbook.save()
    if "Base64" in request.data.keys() :
        base64=data['Base64'][0] 
        newsrc = open('book/image/' + str(addbook.id) + '.txt', 'a')
        newsrc.write(base64)
        newsrc.close()
        
    addbook.bookAvatar = 'book/image/' + str(addbook.id) + '.txt'
    addbook.save()
    return Response({'message': 'New book added'}, status=status.HTTP_201_CREATED)
    


class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        queryset = AddBook.objects.all()
        return queryset




class FilterCategoryaaaa(generics.ListAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = AddBook.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['publication_date', 'genre']



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def show_booksdddd(request):
    books = AddBook.objects.all()
    data = []
    print(books)
    for i in range(len(books)):
        data.append({'id':books[i].id,'name':books[i].title})
    return Response(data , status=status.HTTP_200_OK)





def Delete(request):
    data = dict(request.POST)
    book = AddBook.objects.get(id=data['id'][0])
    if list(book) != []:
        book.delete()
        return Response({'message':'delete complete'})
    else:
        return Response({'message':'you can`t delete'})



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def bookprofile(request):
    if request.method == 'POST':
        data = dict(request.POST)
        book = AddBook.objects.get(id=data['pk'][0])
        serializer = BookSerializer(book)
        return Response(serializer.data)



class BookSearch(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


    def get_queryset(self):
        searchedword = self.request.query_params.get('q', None)
        queryset = AddBook.objects.all()
        if searchedword is None:
            return queryset
        if searchedword is not None:
            if searchedword == "":
                raise Http404
            queryset = queryset.filter(
                Q(title__icontains=searchedword) |
                Q(Description__icontains=searchedword) |
                Q(authors__icontains=searchedword) |
                Q(publisher__icontains=searchedword) 
        )
            if len(queryset) == 0:
                raise Http404
        return queryset


 


class FilterCategory(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []



    def get_queryset(self):
        queryset=AddBook.objects.all()
        genre = self.request.query_params.get('genre', None)
        genre = genre if not genre == '' else None
        publisher = self.request.query_params.get('publisher', None)
        publisher = publisher if not publisher == '' else None
        publication_date__year = self.request.query_params.get('publication_date__year', None)
        publication_date__year = publication_date__year if not publication_date__year == '' else None
        if genre is not None:
            queryset = queryset.filter(genre=genre)
        if publisher is not None:
            queryset = queryset.filter(publisher=publisher)
        if publication_date__year is not None:
            queryset = queryset.filter(publication_date__year=publication_date__year)
        return queryset



        
class RateCreateAPIView(generics.CreateAPIView):
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Rate.objects.filter(book=self.kwargs['pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'user':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Favouritecc(request):
    data = dict(request.POST)
    user = request.user
    book = AddBook.objects.filter(id=request.data['book'])
    if list(book) == []:
        return Response({'message': 'book not found'})
    favourite = Favourite.objects.filter(user=request.user, book=book[0])
    if list(favourite) != []:
        favourite.delete()
        book[0].favourite = False
        book[0].save()
        book[0].favourite_count -=1
        book[0].save()
        return Response({'message': 'favourite is False'}, status=status.HTTP_201_CREATED)
    else:
        favourite = Favourite.objects.create(user=request.user, book=book[0])
        favourite.save()
        book[0].favourite = True
        book[0].save()
        book[0].favourite_count +=1
        book[0].save()
        return Response({'message': 'favourite is True'}, status=status.HTTP_201_CREATED)


class FavouriteCreateAPIView(generics.CreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Rate.objects.filter(book=self.kwargs['pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'user':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class created(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(request):
        if request.method == 'POST':
            data = dict(request.POST)
            book = AddBook.objects.get(id=data['id'][0])
            return book

#------------
#comment
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    #get_replies() function 
   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        account = request.user
        serializer.save(owner= account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReplySerializer
 
    def perform_create(self, serializer):
        mydata = self.request.data 
        user = self.request.user 
        username = user.username 
        commentid = mydata['comment']
        

        thecomments = Comment.objects.filter(id = commentid)
        tcomment = thecomments[0] 
        acc = tcomment.owner 
        
            
        body = f"your comment has been replied by {username};"
      

        print(acc); 
        print(acc.email); 
        notifdata = {}; 
        notifdata['body'] = body
        notifdata['user'] = acc.pk
        datax = {'content': body ,'subject':'notification' ,'to_email':[acc.email]}	
        reply = serializer.save(owner=self.request.user)
        notifdata['replyid'] = reply.id
        # Util.send_email(datax)
        serializer2 = notifserializer(data = notifdata)
        notifdata['isread'] = False
        print(username)
        print(acc.username)

        if serializer2.is_valid() and (username != acc.username ):
            serializer2.save()
        
            

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def addReply(request):
#     data = dict(request.POST)
#     serializer = ReplySerializer(data=request.data)
#     if serializer.is_valid():
#         user = request.user
#         serializer.save(user= user)
#         comment = Comment.objects.filter(id=data['comment'][0])
#         account = comment[0].owner
#         # send_email_content(request , account)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class notifListView(generics.ListAPIView):
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = notifserializer
    def get_queryset(self):
        user = self.request.user
        user_id = user.pk
        queryset = notification.objects.filter(user = user_id)
        return queryset

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def seennotif(request):
    notif_id = request.GET.get("id") 
    notifs = notification.objects.filter(id = notif_id)
    notif = notifs[0] 
    notif.isread = True 
    notif.save() 
    return Response('seen') 


class notifunreadListView(generics.ListAPIView):
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = notifserializer
    def get_queryset(self):
        user = self.request.user
        user_id = user.pk
        queries = notification.objects.filter(user = user_id)
        queryset = queries.filter(isread = False)
        return queryset

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notifdetail(request):
    notif_id = request.GET.get("id") 
    notifs = notification.objects.filter(id = notif_id)
    notif = notifs[0]
    data = {} 
    data['body'] = notif.body 
    data['user'] = request.user.username
    data['isread'] = notif.isread
    data['replyid'] = notif.replyid

    return Response(data = data) 


    
class SavedCreateAPIView(generics.CreateAPIView):
    serializer_class = SavedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Saved.objects.filter(book=self.kwargs['pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'user':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ReadCreateAPIView(generics.CreateAPIView):
    serializer_class = ReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Read.objects.filter(book=self.kwargs['pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'user':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


