from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import forms
from django import forms

class Createuser(UserCreationForm):

   username=forms.CharField(widget=forms.TextInput(attrs={
       "class":"input",
       "type":"",
       "placeholder":"Username"
   }))
   password1=forms.CharField(widget=forms.TextInput(attrs={
       "class":"password",
       "type":"password",
       "placeholder":"Enter Password"
   }))
   password2=forms.CharField(widget=forms.TextInput(attrs={
       "class":"password",
       "type":"password",
       "placeholder":"Confirm Password"
   }))

   class meta:
      model=User
      fields=['username','password1','password2']




class CreateTodo(ModelForm):
   class Meta:
      model=Todo
      fields=['title','status']