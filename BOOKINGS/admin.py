from django.contrib import admin


# Register your models here.
#from .models import manualbooking
class BookingfieldstodisplayinAdmin(admin.ModelAdmin):
    list_display = ('id','ConsignorName','ConsigneeName','TrackingID','BookingDate_date','Picked_Status','PickedStatus_date','Delivered_Status','DeliveredStatus_date','Returned_Status',)
    search_fields = ('TrackingID',)
    list_filter = ('BookingDate_date',)
    list_editable = ('BookingDate_date','Picked_Status','PickedStatus_date','Delivered_Status','DeliveredStatus_date',)
    list_per_page = 50
    
#admin.site.register(manualbooking,BookingfieldstodisplayinAdmin)
