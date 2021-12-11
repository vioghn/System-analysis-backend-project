from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User =get_user_model()

class Contacts(models.Model): 
    user = models.ForeignKey(User , related_name='friends' , on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank = True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    author = models.ForeignKey(Contacts , related_name= 'messages' , on_delete=models.CASCADE )
    content = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content.user.username




class Chats(models.Model): 
    participants = models.ManyToManyField(Contacts , related_name= 'chats' 
    
      )
    Messages = models.ManyToManyField(Message , blank= True)

    def last_10_messages(): 
        return Message.objects.order_by('-timestamp').all()

    def __str__(self):
        return "{}".format(self.pk)











        

