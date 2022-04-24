from pyexpat import model
from re import T
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid

# Create your models here.
class manualbooking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    ConsignorName = models.CharField(max_length=100)
    ConsignorAddress = models.CharField(max_length=100)
    ConsigneeName = models.CharField(max_length=100)
    ConsigneeMobileNumber = models.CharField(max_length=13)
    ConsigneeEmail = models.CharField(max_length=50,blank=True)
    ConsigneeAddress = models.CharField(max_length=50)
    CODAmount = models.IntegerField()
    ProductDetail = models.CharField(max_length=50)
    OriginCity = models.CharField(max_length=50) 
    DestinationCity = models.CharField(max_length=50)
    Weight = models.IntegerField()
    Pieces = models.IntegerField()
    ServiceType = models.CharField(max_length=50)
    SpecialHandling = models.CharField(max_length=50)
    Order_id = models.CharField(max_length=50,blank=True)
    Remarks = models.CharField(max_length=50,blank=True)
    BookingDate_date = models.DateTimeField(default=datetime.now, blank=True)
    Booking_cancelled = models.BooleanField(default=False)
    AddressLabel_Printed = models.BooleanField(default=False)
    AddressLabel_Printed_datetime = models.DateTimeField(null=True, blank=True)
    Loadsheet_Generated = models.BooleanField(default=False)
    Loadsheet_Generated_datetime = models.DateTimeField(null=True, blank=True)
    assigned_to_loadsheet_number = models.IntegerField(null=True)
   #BookingNumber = models.CharField(max_length=50, default=uuid.uuid4)#not generating it anymore 
    Picked_Status = models.BooleanField(default=False)
    PickedStatus_date = models.DateTimeField(null=True, blank=True)
    Delivered_Status = models.BooleanField(default=False)
    DeliveredStatus_date = models.DateTimeField(null=True, blank=True)
    Returned_Status = models.BooleanField(default=False)
    ReturnedStatus_date = models.DateTimeField(default=datetime.now, blank=True)
    pickup_assigned_to_rider = models.CharField(max_length=20,null=True)
    delivery_assigned_to_rider = models.CharField(max_length=20,null=True)
    #instead i am going to pass it into view save method where i will pass businessname+id
    TrackingID = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.ConsigneeName
    #order number https://www.titanwolf.org/Network/q/0727cf05-07ad-4256-b4e6-f6ca53680dd0/y