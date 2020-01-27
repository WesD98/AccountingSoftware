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

	
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
	
	
post_save.connect(create_profile, sender=User)