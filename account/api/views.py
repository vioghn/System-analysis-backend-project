
from django.views import generic
from rest_framework import status 
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from account.api.serializers import RegistrationSerializer, UserSerializer,ChangePasswordSerializer

from django.core import validators
from django.core.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder 
from django.contrib.auth import logout , login
from rest_framework.views import APIView
from account.models import Account
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .utils import Util
import json
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from . import urls
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate



#registering User 
@api_view(['POST', ]) 
@permission_classes([])
@authentication_classes([])  
def registration_view(request):
	try: 
		if request.method == 'POST':
			serializer = RegistrationSerializer(data=request.data)
			data = {}
			if serializer.is_valid():
				account = serializer.save()
				account.is_active = False
				data['response'] = 'successfully registered new user'
				data['email'] = account.email
				data['username'] = account.username
				data['firstname'] = account.firstname
				data['lastname'] = account.lastname
				if(not(account.is_writer)):
					data['status'] = "User"
				else: 
					data['status'] = "Writer"
				

				token = Token.objects.get(user=account).key
				data['token'] = token
				send_email_content(token , request , account)
				
			else:
				data = serializer.errors

			return Response(data)

	except KeyError as e:
		print(e)
		raise ValidationError({"400": f'Field {str(e)} missing'})



#sending Email FUnction 
def send_email_content(token , request , account):
	current_site = get_current_site(request).domain
	reletivelink = reverse('account:verification')	
	absurl='http://' + current_site +reletivelink + "?token=" +str(token)
	email_body = 'use link below to verify your email\n' + 'domain:' + absurl
	data = {'content':email_body ,'subject':'please verify you email' ,'to_email':[account.email]}	
	Util.send_email(data)	


#activating user account
@api_view(['GET', ]) 
@permission_classes([])
@authentication_classes([]) 
def verification( request):
	
	token=request.GET.get('token')
	try:
	
		myuser= Token.objects.get(key=token).user
		id = myuser.pk
		user = Account.objects.get(pk = id)
		
		
	except(TypeError, ValueError, OverflowError, Token.DoesNotExist):
		token1=None
		return Response('Token is invalid or expired. Please request another confirmation email by signing in.', status=status.HTTP_400_BAD_REQUEST)
	
	except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
		user = None 
		if user is None:
			return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
	
	
	user.is_active = True
	user.save()
	return Response('Email successfully confirmed') 

#login user function based view 
@api_view(["POST"])
def login_user(request):

        data = {}
        reqBody = json.loads(request.body)
        email1 = reqBody["email"]
        print(email1)
        password = reqBody["password"]
        try:
            Accounts = Account.objects.get(email=email1)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})
		
        token = Token.objects.get_or_create(user=Accounts)[0].key
		
        if(not(Accounts.check_password( password))):
            raise ValidationError({"message": "password is incorrect"})

        if Account:
            if Accounts.is_active:
                print(request.user)
                login(request, Accounts)
				
                data["message"] = "user logged in"
                data["email"] = Accounts.email

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account is not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})


#loging out user 
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

	if(request.user.IsAuthenticated):
		request.user.auth_token.delete()
		logout(request)
		return Response('User Logged out successfully')
	else:
		return Response('User is not logged in')


#user properties 
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def User_API(request):

	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(account)
		return Response(serializer.data)

#User updating account 
@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def update_account_view(request):

	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'PUT':
		serializer = UserSerializer(account, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = 'Account update success'
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#check passsword to be completed 
















































































































































































































































































































def validate_email(email):
	account = None
	try:
		account = Account.objects.get(email=email)
	except Account.DoesNotExist:
		return None
	if account != None:
		return email

def validate_username(username):
	account = None
	try:
		account = Account.objects.get(username=username)
	except Account.DoesNotExist:
		return None
	if account != None:
		return username

class ObtainAuthTokenView(APIView):

	authentication_classes = []
	permission_classes = []

	def post(self, request):
		context = {}

		username = request.POST.get('username')
		password = request.POST.get('password')
		account = authenticate(username=username, password=password)
		if account:
			try:
				token = Token.objects.get(user=account)
			except Token.DoesNotExist:
				token = Token.objects.create(user=account)
			context['response'] = 'Successfully authenticated.'
			context['pk'] = account.pk
			context['username'] = username.lower()
			context['token'] = token.key
		else:
			context['response'] = 'Error'
			context['error_message'] = 'Invalid credentials'

		return Response(context)

@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def does_account_exist_view(request):

	if request.method == 'GET':
		email = request.GET['email'].lower()
		data = {}
		try:
			account = Account.objects.get(email=email)
			data['response'] = email
		except Account.DoesNotExist:
			data['response'] = "Account does not exist"
		return Response(data)



# class ChangePasswordView(UpdateAPIView):

# 	serializer_class = ChangePasswordSerializer
# 	model = Account
# 	permission_classes = (IsAuthenticated,)
# 	authentication_classes = (TokenAuthentication,)

# 	def get_object(self, queryset=None):
# 		obj = self.request.user
# 		return obj

# 	def update(self, request, *args, **kwargs):
# 		self.object = self.get_object()
# 		serializer = self.get_serializer(data=request.data)

# 		if serializer.is_valid():
# 			# Check old password
# 			if not self.object.check_password(serializer.data.get("old_password")):
# 				return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

# 			# confirm the new passwords match
# 			new_password = serializer.data.get("new_password")
# 			confirm_new_password = serializer.data.get("confirm_new_password")
# 			if new_password != confirm_new_password:
# 				return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)

# 			# set_password also hashes the password that the user will get
# 			self.object.set_password(serializer.data.get("new_password"))
# 			self.object.save()
# 			return Response({"response":"successfully changed password"}, status=status.HTTP_200_OK)

# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



