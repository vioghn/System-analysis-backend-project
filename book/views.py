from book.models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from .models import AddBook
from .serializers import BookSerializer
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.http import response


@ login_required
def favourite_list(request):
    new = Book.newmanager.filter(favourites=request.user)
    return response(new)
   # return render(request,
   # 'accounts/favourites.')


@ login_required
def favourite_add(request, id):
    book = get_object_or_404(Book, id=id)
    if book.favourites.filter(id=request.user.id).exists():
       book.favourites.remove(request.user)
    else:
        book.favourites.add(request.user)
    return HttpResponseRedirect(request.Meta['HTTP_REFERER'])

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



class ShopSearch(generics.ListAPIView):
    serializer_class = ShopSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        searchedword = self.request.query_params.get('q', None)
        queryset = Shop.objects.all()
        if searchedword is None:
            return queryset
        if searchedword is not None:
            if searchedword == "":
                raise Http404
            queryset = queryset.filter(
                Q(titleicontains=searchedword) |
                Q(addressicontains=searchedword)
            )
            if len(queryset) == 0:
                raise Http404
        return queryset




class FilterCategoryItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = Item.objects.filter(category=q)
        return queryset