from django.db import models
from datetime import datetime

# Create your models here.
#class Users(models.Model):
    #firstname = models.CharField(max_length=100)
    #lastname = models.CharField(max_length=100)
    #username = models.CharField(max_length=100)
    #phone = models.CharField(max_length=13)
    #email = models.CharField(max_length=50)
    #verified = models.BooleanField(default=False)
    #reg_date = models.DateTimeField(default=datetime.now, blank=True)
    #def __str__(self):
     #   return self.username

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    businessname = models.CharField(max_length=50, blank=True)
    businessaddress = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    areapostalcode = models.CharField(max_length=50, blank=True)
    natureofbusiness = models.CharField(max_length=50, blank=True)
    numberofshipmentspermonth = models.CharField(max_length=50, blank=True)
    sellingplatform = models.CharField(max_length=50, blank=True)
    sellingplatformlink = models.CharField(max_length=50, blank=True)
    cnic_ntn = models.CharField(max_length=50, blank=True)
    information_filled=models.BooleanField(default=False)
    profile_verified=models.BooleanField(default=False)
    #BENEFICIARY_NAME = models.CharField(max_length=50, blank=True)	
    #BENEFICIARY_BANK_ACC_NO = models.CharField(max_length=20, blank=True)
    #BANK_NAME	models.CharField(max_length=20, blank=True)

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
