
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from account.api.serializers import RegistrationSerializer
from django.core import validators
from django.core.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder 

 
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
				token = Token.objects.get(user=account).key
				data['token'] = token
			else:
				data = serializer.errors
			return Response(data)

	except KeyError as e:
		print(e)
		raise ValidationError({"400": f'Field {str(e)} missing'})



# @api_view(["POST"])
# @permission_classes([AllowAny])
# def login_user(request):

#         data = {}
#         reqBody = json.loads(request.body)
#         email1 = reqBody['email']
#         print(email1)
#         password = reqBody['password']
#         try:

#             Account = Account.objects.get(email=email1)
#         except BaseException as e:
#             raise ValidationError({"400": f'{str(e)}'})

#         token = Token.objects.get_or_create(user=Account)[0].key
#         print(token)
#         if not check_password(password, Account.password):
#             raise ValidationError({"message": "Incorrect Login credentials"})

#         if Account:
#             if Account.is_active:
#                 print(request.user)
#                 login(request, Account)
#                 data["message"] = "user logged in"
#                 data["email_address"] = Account.email

#                 Res = {"data": data, "token": token}

#                 return Response(Res)

#             else:
#                 raise ValidationError({"400": f'Account not active'})

#         else:
#             raise ValidationError({"400": f'Account doesnt exist'}