from rest_framework import serializers
from account.models import Account
from django.core.serializers.json import DjangoJSONEncoder 
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os
from .utils import  is_image_size_valid
IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2 # 2MB

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields  = ['pk', 'image',  'firstname', 'lastname','username' , 'bio' , 'province' ,
		 'gender' , 'phone_number' , 'date_birth' , 'isstory' , 'issocial' , 'ishistoric' , 'isarty' , 'ispsychology' , 'isscientific']
	


class UserSerializerothers(serializers.ModelSerializer):
	class Meta:
		model = Account
		
		fields  = ['pk', 'image',  'firstname', 'lastname','username' , 'bio']


	def validate(self, user):
		try:
			
			image = user['image']
			url = os.path.join(settings.TEMP , str(image))
			storage = FileSystemStorage(location=url)

			with storage.open('', 'wb+') as destination:
				for chunk in image.chunks():
					destination.write(chunk)
				destination.close()

			# Check image size
			if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
				os.remove(url)
				raise serializers.ValidationError({"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

	
			os.remove(url)
		except KeyError:
			pass
		return user
			

class UserSerializerwithoutusername(serializers.ModelSerializer):

	class Meta:
		model = Account
		
		fields  = ['pk', 'image',  'firstname', 'lastname','username' , 'bio' ,
		 'province' , 'gender' , 'phone_number' , 'date_birth' , 'isstory' , 'issocial' , 'ishistoric' , 'isarty' , 'ispsychology' , 'isscientific'  ]
	


	def validate(self, user):
		try:
			
			image = user['image']
			url = os.path.join(settings.TEMP , str(image))
			storage = FileSystemStorage(location=url)

			with storage.open('', 'wb+') as destination:
				for chunk in image.chunks():
					destination.write(chunk)
				destination.close()

			# Check image size
			if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
				os.remove(url)
				raise serializers.ValidationError({"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

	
			os.remove(url)
		except KeyError:
			pass
		return user

	

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

        
        



