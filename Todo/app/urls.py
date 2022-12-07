from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.home,name='home'),
     path('loginpage', views.loginpage,name='loginpage'),
     path('signup', views.signup,name='signup'),
     path('logout', views.logoutpage,name='logout'),
     path('create', views.createtodo,name='create'),
     path('delete/<int:id>', views.deletetodo,name='delete'),
     path('update/<int:id>', views.updatetodo,name='update'),
]