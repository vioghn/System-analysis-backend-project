from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView 
from django.http import Http404
from .models import AddBook
from .serializers import BookSerializer
from rest_framework import filters,generics,status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q  


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def bookprofile(request):
    if request.method == 'POST':
        data = dict(request.POST)
        book = AddBook.objects.get(id=data['id'][0])
        serializer = BookSerializer(book)
        return Response(serializer.data)