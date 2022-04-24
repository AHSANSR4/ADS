from django.contrib.auth import models
from django.http import request
from django.contrib.auth.decorators import login_required
from django.http.request import split_domain_port
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User
from .models import manualbooking
from HOME.models import Profile
from datetime import date

# Create your views here.
#you can do this in your view works fine for me without declaring in settings.py
#https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
 #redirect when user is not logged in
@login_required(login_url='login')#https://docs.djangoproject.com/en/3.2/topics/auth/default/
def manualbookings(request) :
    if request.method == 'POST':
        CODAmount = request.POST['codamount']
        CODAmount=int(CODAmount)
        if(CODAmount >= 30000):
          messages.error(request,'ORDER MORE THAN 30,000 NEED ADVANCED PAYMENT PLEASE CONTACT ADMIN HELP')
          return redirect('BOOKINGS')
        else:
            ConsignorName = request.POST['consignorname']
            ConsignorAddress = request.POST['consignoraddress']
            ConsigneeName = request.POST['consigneename']
            ConsigneeMobileNumber = request.POST['consigneemobilenumber']
            ConsigneeEmail = request.POST['consigneeemail']
            ConsigneeAddress = request.POST['Consigneeaddress']
            ProductDetail = request.POST['productdetail']
            OriginCity = request.POST['origincity']
            DestinationCity	= request.POST['destinationcity']
            Weight = request.POST['weight']
            Pieces= request.POST['pieces']
            ServiceType = request.POST['servicetype']
            SpecialHandling = request.POST['specialhandling']
            Order_id = request.POST['Order_id']
            Remarks	= request.POST['remarks']
            user_id	= request.POST['userid']
            
            TrackingIDUsername = request.user.get_username()#here i'm getting username of the loggged in user
            
            TrackingIDlastID = manualbooking.objects.order_by('TrackingID').last()
            #above i'm getting the last tracking id so that i can increment it and pass it to the model
            TrackingIDlastID=str(TrackingIDlastID.id+1)#here i converted it into string and incremented it with one(+1)
            #One thing to note is that Python cannot concatenate a string 
            #and integer. These are considered two separate types of objects. So, if you want to merge the two,
            # you will need to convert the integer to a string
            TrackingID = TrackingIDUsername+"00"+TrackingIDlastID        
            #print(ConsignorName,ConsignorAddress,ConsigneeName,ConsigneeMobileNumber,ConsigneeEmail,ConsigneeAddress,CODAmount,ProductDetail,OriginCity,DestinationCity,Weight,Pieces,ServiceType,SpecialHandling,Remarks)
            manualbookings = manualbooking(ConsignorName=ConsignorName,ConsignorAddress=ConsignorAddress,ConsigneeName=ConsigneeName,
                  ConsigneeMobileNumber=ConsigneeMobileNumber,ConsigneeEmail=ConsigneeEmail,ConsigneeAddress=ConsigneeAddress,CODAmount=CODAmount,ProductDetail=ProductDetail,
                  OriginCity=OriginCity,DestinationCity=DestinationCity,Weight=Weight,Pieces=Pieces,ServiceType=ServiceType,
                        SpecialHandling=SpecialHandling,Order_id=Order_id,Remarks=Remarks,user_id=user_id,TrackingID=TrackingID)
            manualbookings.save()          
            messages.success(request,'BOOKED SUCCESSFULLY')
            return redirect('BOOKINGS')
            #No matter how many problems you face, solving them is what makes life worth living. There’s always a solution.

    else:    
        return render(request,'BOOKINGS/manualbookings.html') 

@login_required(login_url='login')
def bookingreceipt(request,id):    
        getreceipt = get_object_or_404(manualbooking,pk=id) #pk=ad_id is what we passed in our urls.py
        context={'getreceipt':getreceipt}
        return render(request,'BOOKINGS/bookingreceipt.html',context)   


@login_required(login_url='login')
def printlabel(request,id):
        printlabel = get_object_or_404(manualbooking,pk=id) #pk=ad_id is what we passed in our urls.py
        printlabel.AddressLabel_Printed=True #updating the AddressLabel_Printed field in database to True
        printlabel.save() #query to update the field in database
        context={'PL':printlabel}
        return render(request,'BOOKINGS/printlabel.html',context)  



@login_required(login_url='login')
def printlabels(request):
       return render(request,'BOOKINGS/printlabels.html',)        


@login_required(login_url='login')
def printaddresslabels(request):
      userid=request.user.id#fetching loggedin user id 
      userid=str(userid)#converting user id into string to pass it inside/alongwith url
      if 'search' in request.GET: # first check if search exists in the searched and this form is a GET request 
            data = manualbooking.objects.order_by('TrackingID')
            search = request.GET['search'] # created a variable , and getting the actual form value 
            if search: # to check if its not an empty string
                search = data.filter(TrackingID__iexact=search,user_id=userid) 
                print(search)
                context={'PAL':search,}
                return render(request,'BOOKINGS/printaddresslabels.html',context) 
      if 'printselected' in request.GET:
             selected_values = request.GET.getlist('foo')#getting the selected value that we passed by get method in our template 
             selected_values = manualbooking.objects.filter(id__in=selected_values) #filtering the data by the ids that we got in our url
             TSV=len(selected_values)#totalselectedvalues length
             #A QuerySet represents a collection of objects from your database. It can have zero, one or many filters.
             #since selected_values is a queryset & a queryset isn't a single object, 
             # it's a group of objects so it doesn't make sense to call save() on a queryset.
             #Instead we will save each individual object IN the queryset using for loop:
                  
             for i in selected_values:
                  i.AddressLabel_Printed=True #updating the AddressLabel_Printed field in database to True
                  i.save() #updating the values one by one 
             #doing the same what we did in above printlabel function when a user selects multiple id and 
             # pass it to printlabels we will update the table field AddressLabel_Printed = true

             #PSV stands for print selected values
             context={'PSV':selected_values,'tsv':TSV}
            # printselected = request.GET['printselected'] # created a variable , and getting the selected checkbox form value
             return render(request,'BOOKINGS/printlabels.html',context) 

      if 'fromdate' in request.GET:
            
            fromdate = request.GET['fromdate'] # created a variable , and getting the selected fromdate from url
            todate = request.GET['todate'] # created a variable , and getting the selected todate from url
            if not todate:
                  todate = date.today() 
                  
            FTD = manualbooking.objects.filter(BookingDate_date__range=[fromdate, todate]) 
            print(FTD)
            context={'PAL':FTD,}
            return render(request,'BOOKINGS/printaddresslabels.html',context)             
                      
      else:      
            printaddresslabels = manualbooking.objects.order_by('-BookingDate_date')
            #printaddresslabels = printaddresslabels.filter(user_id=userid,AddressLabel_Printed=False)
            printaddresslabels = printaddresslabels.filter(user_id=userid)
            context={'PAL':printaddresslabels,}
            return render(request,'BOOKINGS/printaddresslabels.html',context) 


@login_required(login_url='login')#https://docs.djangoproject.com/en/3.2/topics/auth/default/
def loadsheet(request):
      return render(request,'BOOKINGS/loadsheet.html',)


@login_required(login_url='login')#https://docs.djangoproject.com/en/3.2/topics/auth/default/
def TotalBookings(request):
      return render(request,'BOOKINGS/TotalBookings.html',)  


@login_required(login_url='login')#https://docs.djangoproject.com/en/3.2/topics/auth/default/
def MonthlyTotalBookings(request):
      return render(request,'BOOKINGS/MonthlyTotalBookings.html',)  


@login_required(login_url='login')#https://docs.djangoproject.com/en/3.2/topics/auth/default/
def TodayTotalBookings(request):
      return render(request,'BOOKINGS/TodayTotalBookings.html',)  
