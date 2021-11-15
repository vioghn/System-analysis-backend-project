from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import AddBook
from .serializers import BookSerializer
from rest_framework import filters,generics,status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

@api_view(['POST'])
def add_book(request):
    data = dict(request.POST)
    print(data)
    addbook = AddBook.objects.create(      
        title=data['title'][0],
        genre=data['genre'][0],
        authors=data['authors'][0],
        publisher=data['publisher'][0],
        publication_date=data['publication_date'][0],
    )
    addbook.save()
    if "Description" in request.data.keys() :
        addbook.Description=data['Description'][0]
    addbook.save()
    return Response({'message': 'New book added'}, status=status.HTTP_201_CREATED)
    


@api_view(['POST'])
def show_books(request):
    books = AddBook.objects.all()
    data = []
    print(books)
    for i in range(len(books)):
        data.append({'id':books[i].id,'name':books[i].title})
    return Response(data , status=status.HTTP_200_OK)



class BookSearch(generics.ListAPIView):
    serializer_class = BookSerializer



    def get_queryset(self):
        searchedword = self.request.query_params.get('q', None)
        queryset = AddBook.objects.all()
        print("searchedword",searchedword)
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

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = AddBook.objects.filter(Q(genre=q) | Q(publication_date=q))
        return queryset

