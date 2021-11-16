from django.urls import path

from . import views

urlpatterns = [
    
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favorites/', views.favourite_list, name='favourite_list'),


]