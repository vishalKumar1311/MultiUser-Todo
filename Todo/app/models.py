from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
       status_choice= [
         ( '✅', 'Completed'),
          ('⏳', 'Pending'),
         ]
       user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
       title= models.CharField(max_length=30)
       status= models.CharField(max_length=2,choices=status_choice)
       date=models.DateField(auto_now_add=True)
       
       
 