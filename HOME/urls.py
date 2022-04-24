from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.models import User
from django.http import request



def sample_view(request):
    current_user = request.user
    user_id=current_user.id

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('complete_registration/<int:user_id>/', views.complete_registration, name='complete_registration'),
]