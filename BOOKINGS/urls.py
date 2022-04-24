from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.manualbookings, name='BOOKINGS'),
    path('<int:id>', views.bookingreceipt, name='bookingreceipt'),
    path('printlabel/<int:id>', views.printlabel, name='printlabel'),
    path('printlabels', views.printlabels, name='printlabels'),
    path('printaddresslabels', views.printaddresslabels, name='printaddresslabels'),
    path('loadsheet', views.loadsheet, name='loadsheet'),
    path('TotalBookings', views.TotalBookings, name='Totalbookings'),
    path('TodayTotalBookings', views.TodayTotalBookings, name='bookingreceipt'),
    path('MonthlyTotalBookings', views.MonthlyTotalBookings, name='bookingreceipt'),
    
   
]