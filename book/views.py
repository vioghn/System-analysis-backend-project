from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import AddBook
from .serializers import BookSerializer


@api_view(['POST'])
def addbook(request):
    data = dict(request.POST)
    print(data)
    addbook = AddBook.objects.create(
        selectedTopic=data['selectedTopic'][0],
        title=data['title'][0],
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
