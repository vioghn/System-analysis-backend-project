from rest_framework import serializers
from account.models import Account
from django.core.serializers.json import DjangoJSONEncoder 
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ('username', 'email' , 'password') 
	
	def current_user(self): 
		try:
			return Account.objects.get(email=self.validated_data['email'])
		except ObjectDoesNotExist:
			raise ValidationError({"400": f'Account doesnt exist'})
	def get_password(self):
			return self.validated_data['password']

	
	


class RegistrationSerializer(serializers.ModelSerializer):

	password2 	= serializers.CharField(style={'input_type': 'password'}, write_only=True)
	# writer 	= serializers.CharField()
	class Meta:
		model = Account
		fields = ['firstname' , 'lastname','email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}


	def	save(self,  *args, **kwargs):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)

		account.firstname = self.validated_data['firstname'] 
		account.lastname = self.validated_data['lastname']
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		 
		account.save()
		# account.create(self.validated_data)
    
		return account

        
        



