from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics
from rest_framework.response import Response
from django.http import Http404
from .models import AddBook
from .serializers import BookSerializer

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
                return Http404
            queryset = queryset.filter(title=searchedword)
            if len(queryset) == 0:
                return Http404
        return queryset


class Search(ModelViewSet):
    queryset = AddBook.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title')



class FilterCategory(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = AddBook.objects.all()
        return queryset

