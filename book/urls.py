from django.urls import path

from . import views

urlpatterns = [
    path("addbook/", views.addbook, name="addbook"),
    path("loadbook/", views.show_books, name="show_books"),

]