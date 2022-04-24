from django.core.checks.messages import Error
from django.db import reset_queries
from django.shortcuts import redirect, render 
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from BOOKINGS.models import manualbooking
from BOOKINGS.views import manualbookings
from datetime import date, timedelta, timezone
from django.utils.timezone import now
from datetime import datetime
from .models import Profile


# Create your views here.

def index(request) :
        userid=request.user.id#fetching loggedin user id 
        if Profile.objects.filter(user_id=userid,information_filled=True,profile_verified=False):
            information_filled="FALSE"
            context={'information_filled':information_filled}
            return render(request,'home/index.html',context)
          
        return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')  

def register(request):
        if request.user.is_authenticated:
           #messages.info(request,'YOU ARE ALREADY REGISTERED & LOGGED IN')
           return redirect('dashboard')
        else:
            if request.method == 'POST':
                #LOGIC HERE
                #so first we will put everthing into variable every form field submitted will be put in variable
                #getting form values
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                username = request.POST['username']
                phone = request.POST['phone']
                email = request.POST['email']
                password = request.POST['password']
                password2 = request.POST['password2']
                #check if passwords match
                if password == password2:
                    #check username
                    if User.objects.filter(username=username).exists():
                        messages.error(request,'Username Already Taken')
                        return redirect('register')
                    else:
                        if User.objects.filter(email=email).exists():
                            messages.error(request,'THIS EMAIL IS  ALREADY IN USE')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(username=username,
                            email=email,password=password,first_name=first_name,last_name=last_name)
                            auth.login(request, user)
                            messages.success(request,'SUCCESSFULLY REGISTERED , COMPLETE THE REMAINING REGISTRATION ')
                            return redirect('dashboard')
                else:    
                    #show passwordsw don't match error 
                    messages.error(request,'Passwords Do not match')
                    return redirect('register')
            else:
                return render(request,'home/register.html')

def login(request):
     if request.user.is_authenticated:
           messages.success(request,'YOU ARE ALREADY LOGGED IN')
           return redirect('dashboard')
     else:
            if request.method == 'POST':
                #Login USER
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    messages.success(request,'YOU ARE NOW LOGGED IN')
                    return redirect('dashboard')
                else:
                    messages.error(request,'INVALID USERNAME OR PASSWORD')
                    return redirect('login')
            else:
                return render(request,'home/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'LOGOUT SUCCESSFUL')
    return redirect('login')   

def dashboard(request):
        userid=request.user.id#fetching loggedin user id 
        if Profile.objects.filter(user_id=userid,information_filled=False):#passing the logged in user id and then filtering if he has submited the information
            
            userid=str(userid)#converting user id into string to pass it inside/alongwith url
            messages.info(request,'YOUR ACCOUNT IS NOT VERIFIED')
            return redirect('complete_registration/'+userid)
        else:
            userid=request.user.id #fetching user id 
            #SR=manualbooking.objects.raw('select all from manualbooking where BookingDate_date between "'+FD+'" and "'+TD+'"')
            MTB=manualbooking.objects.order_by('-BookingDate_date').filter(user_id=userid)
            P=manualbooking.objects.filter(user_id=userid, Picked_Status=True , Delivered_Status=False)
            D=manualbooking.objects.filter(user_id=userid, Picked_Status=True, Delivered_Status=True )
            P=len(P)
            D=len(D)
            MTBCOUNT=len(MTB)
            context={'MTBCOUNT':MTBCOUNT,'MTB':MTB,'P':P,'D':D,}
            print(MTB,request.user.id,)
            return render(request,'home/dashboard.html',context)     

def complete_registration(request,user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
                #LOGIC HERE
                #so first we will put everthing into variable every form field submitted will be put in variable
                #getting form values
                businessname = request.POST['businessname']
                businessaddress = request.POST['businessaddress']
                country = request.POST['country']
                city = request.POST['city']
                postalcode = request.POST['postalcode']
                nob = request.POST['nob']
                nospm = request.POST['nospm']
                sellingplatform = request.POST['sellingplatform']
                loysp = request.POST['loysp']
                cnic = request.POST['cnic']
                print(businessname,businessaddress,country,city,postalcode,nob,nospm,sellingplatform,loysp,cnic)
                user.profile.businessname=businessname
                user.profile.businessaddress=businessaddress=businessaddress
                user.profile.country=country
                user.profile.city=city
                user.profile.areapostalcode=postalcode
                user.profile.natureofbusiness=nob
                user.profile.numberofshipmentspermonth=nospm
                user.profile.sellingplatform=sellingplatform
                user.profile.sellingplatformlink=loysp
                user.profile.cnic_ntn=cnic
                user.profile.information_filled=True
                user.save()

                messages.success(request,'SUCCESSFULY SUBMITED NOW WAIT FOR VERIFICATION APPROVAL'+businessname)
                return redirect('dashboard')
    else:
        return render(request,'home/complete_registration.html')   
     