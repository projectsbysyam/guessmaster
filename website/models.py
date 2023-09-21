from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_agent = models.BooleanField("is agent", default=False)
    is_dealer = models.BooleanField("is dealer", default=False)

class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="agent")
    agent_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return str(self.agent_name)
    
class Dealer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="dealer")
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    dealer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dealer_name)