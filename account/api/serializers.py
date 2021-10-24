from rest_framework import serializers
from account.models import Account

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email') 


class RegistrationSerializer(serializers.ModelSerializer):

	password2 	= serializers.CharField(style={'input_type': 'password'}, write_only=True)
	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}


	
	def create(self, validated_data):
		return Account.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        
        


def	save(self,  *args, **kwargs):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		# account.create(self.validated_data)
    
		return account

