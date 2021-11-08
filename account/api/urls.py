from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from account.api import views
from account.api.views import(
	registration_view,

)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('register/', registration_view, name="register"),
	path('login/', obtain_auth_token, name="login"),
	path('logout/', views.User_logout, name="logout"),
	path('properties/', views.User_API, name="properties"),
	path('verification' , views.VerifyEmail.as_view(), name="verification")
]
urlpatterns = format_suffix_patterns(urlpatterns)