from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
class ProfilefieldstodisplayinAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','businessname','businessaddress','country','city','areapostalcode','natureofbusiness','numberofshipmentspermonth','sellingplatform','sellingplatformlink','cnic_ntn','information_filled','profile_verified',)
    search_fields = ('businessname','user_id',)
    list_filter = ('businessname',)
    list_editable = ('profile_verified','businessname',)
    list_per_page = 50
    
admin.site.register(Profile,ProfilefieldstodisplayinAdmin)

# Register your models here.
#from  .models import Users
#class HomeAdmin(admin.ModelAdmin):
#    list_display = ('id','username','phone','email','reg_date',)
#admin.site.register(Users,HomeAdmin)
