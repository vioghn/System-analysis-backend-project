
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from account.api.serializers import RegistrationSerializer, UserSerializer
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

import json


 
@api_view(['POST', ]) 
    
def registration_view(request):
	try: 
		if request.method == 'POST':
			serializer = RegistrationSerializer(data=request.data)
			data = {}
			if serializer.is_valid():
				account = serializer.save()
				data['response'] = 'successfully registered new user.'
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
			else:
				data = serializer.errors
			return Response(data)

	except KeyError as e:
		print(e)
		raise ValidationError({"400": f'Field {str(e)} missing'})


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



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

	if(request.user.IsAuthenticated):
		request.user.auth_token.delete()
		logout(request)
		return Response('User Logged out successfully')
	else:
		return Response('User is not logged in')


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_API(request, user): 
	

	try:
		user = Account.objects.get(user = user)
	except user.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)	


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_APIxx(request , token): 
	
	try:
		user = Token.objects.get(key=token).user
		user = Account.objects.get(user = user)
	except user.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)

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