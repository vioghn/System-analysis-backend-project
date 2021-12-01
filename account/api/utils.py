from re import sub
from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        email =EmailMessage(subject = data['subject'], body= data['content'] , to=data['to_email'])
        email.send()




def is_image_size_valid(img_url, mb_limit):
	image_size = os.path.getsize(img_url)
	# print("image size: " + str(image_size))
	if image_size > mb_limit:
		return False
	return True

