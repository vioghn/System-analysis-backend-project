from django.urls import path
from .views import BookSearch, FilterCategory, BookListView, RateCreateAPIView, notifListView
from . import views

urlpatterns = [
    path("addbook/", views.add_book, name="addbook"),
    path("loadbook/", views.BookListView.as_view(), name="BookListView"),
    path("bookprofile/", views.bookprofile, name="bookprofile"),
    path("delete/", views.Delete, name="Delete"),
    #path('bookprofile/<int:id>/', views.bookprofile.as_view(), name='delete'),
    path('search/', views.BookSearch.as_view(), name="BookSearch"),
    path('category/', views.FilterCategory.as_view(), name="FilterCategory"),
    path('comments/' , views.CommentList.as_view(), name="comments"),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = "comment-detail"),
    path('rate/create/', views.RateCreateAPIView.as_view(), name="RateCreate"),
    path('favourite/create/', views.Favouritecc, name="Favouritecc"),
    path('replycomment/' , views.ReplyList.as_view(), name="reply"),
    path('replycomment/<int:pk>/', views.ReplyDetail.as_view(), name = "reply-detail"),
    path('notif/list/', views.notifListView.as_view(), name ="notification"),
    path('notif/unreed/', views.notifunreadListView.as_view(), name ="notification"),
    path('notifdetail/', views.notifdetail, name ="notification"),
    path('notifseen/', views.seennotif, name ="notification"),
    path('read/create/', views.read, name="ReadCreateAPIView"),
    path('saved/create/', views.savebook, name="savedCreateAPIView"),  
    
]



