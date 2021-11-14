from django.urls import path

from . import views

urlpatterns = [
    path("addbook/", views.add_book, name="addbook"),
    path("loadbook/", views.show_books, name="show_books"),
    ##path("searchbook/", views.search_book, name="search_book"),
    re_path('^searchbook/(?P<username>.+)/$', BookSearch.as_view()),
]