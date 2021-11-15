from django.urls import path
from .views import BookSearch, FilterCategory
from . import views

urlpatterns = [
    path("addbook/", views.add_book, name="addbook"),
    path("loadbook/", views.show_books, name="show_books"),
    path('booksearch/', BookSearch.as_view(), name="BookSearch"),
    #path('search/', search.as_view(), name="BookSearch"),
    path('category/', FilterCategory.as_view(), name="FilterCategory"),
]



