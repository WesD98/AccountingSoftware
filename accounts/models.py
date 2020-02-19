from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to='profile_image', blank=True)
	address = models.CharField(max_length=200, default='')
	DOB = models.CharField(max_length=20, default='')

class AccountM(models.Model):
    
    Account_Name = models.CharField(max_length=100, primary_key=True)
    Account_Type = models.CharField(max_length=60, default="")
    Account_Description = models.CharField(max_length=200)
    Account_Number = models.IntegerField(default=0)
    Account_Category = models.CharField(max_length=60)
    Account_Sub_Category = models.CharField(max_length=60)
    Account_Initial_Balance = models.DecimalField(max_digits=20, decimal_places=2)
    Account_Credit = models.DecimalField(max_digits=20, decimal_places=2)
    Account_Balance = models.DecimalField(max_digits=20, decimal_places=2)
    Order = models.CharField(max_length=60)
    Statements = models.FileField(upload_to = 'StatementsFile') 
    Comments = models.CharField(max_length=60)
    Date_Added = models.DateField(auto_now=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
	
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
	
	
post_save.connect(create_profile, sender=User)