from django.urls import path
from .views import BookSearch, FilterCategory, show_books, bookprofile
from . import views

urlpatterns = [
    path("addbook/", views.add_book, name="addbook"),
    path("loadbook/", views.show_books.as_view(), name="show_books"),
    path("bookprofile/", views.bookprofile.as_view(), name="bookprofile"),
    #path('bookprofile/<int:id>/', views.bookprofile.as_view(), name='delete'),
    path('search/', views.BookSearch.as_view(), name="BookSearch"),
    path('category/', FilterCategory.as_view(), name="FilterCategory"),
]



