from rest_framework import serializers
from account.models import Account
from django.core.serializers.json import DjangoJSONEncoder 
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = fields = ['pk', 'image',  'firstname', 'lastname','username']


	# def validate_username(self, value):
	# 	user = self.context['request'].user
	# 	if Account.objects.exclude(pk=user.pk).filter(username=value).exists():
	# 		raise serializers.ValidationError({"username": "This username is already in use."})
	# 	return value



	# def update(self, instance, validated_data):
	# 	instance.first_name = validated_data['first_name']
	# 	instance.last_name = validated_data['last_name']
	# 	instance.username = validated_data['username']
	# instance.save()

    #     return instance
	

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

#to be completed 
class ChangePasswordSerializer(serializers.Serializer):

	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)

        
        



