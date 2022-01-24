from re import sub
from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        email =EmailMessage(subject = data['subject'], body= data['content'] , to=data['to_email'])
        email.send()
