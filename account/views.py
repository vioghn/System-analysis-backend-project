from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from book.models import Book
# Createour views here.



@ login_required
def favourite_add(request, id):
    book = get_object_or_404(Book, id=id)
    if book.favourites.filter(id=request.user.id).exists():
        book.favourites.remove(request.user)
    else:
        book.favourites.add(request.user)
    return HttpResponseRedirect(request.Meta['HTTP_REFERER'])
