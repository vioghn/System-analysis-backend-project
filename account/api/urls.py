from django.core.exceptions import ViewDoesNotExist
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from account.api import views
from account.api.views import(
	DeleteAccount,
	registration_view,

)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('check_if_account_exists/', views.does_account_exist_view, name="check_if_account_exists"),
	path('register/', registration_view, name="register"),
	path('login/', views.ObtainAuthTokenView.as_view(), name="login"),
	path('logout/', views.User_logout, name="logout"),
	path('properties/', views.User_API, name="properties"),
	path('properties/update/', views.update_account_view, name="update"),
	path('verification/' , views.verification, name="verification"),
	path('DeleteAccount', views.DeleteAccount.as_view(),name="DeleteAccount" )
]
urlpatterns = format_suffix_patterns(urlpatterns)