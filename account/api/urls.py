from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from account.api import views
from account.api.views import(
	registration_view,

)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('check_if_account_exists/', views.does_account_exist_view, name="check_if_account_exists"),
	path('change_password/', views.ChangePasswordView.as_view(), name="change_password"),
	path('register/', registration_view, name="register"),
	path('login/', obtain_auth_token, name="login"),
	path('logout/', views.User_logout, name="logout"),
	path('properties/', views.User_API, name="properties"),
	path('properties/update', views.User_API, name="update"),
	path('verification/' , views.verification, name="verification")
]
urlpatterns = format_suffix_patterns(urlpatterns)