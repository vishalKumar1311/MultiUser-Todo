from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from app.forms import CreateTodo,Createuser
from django.urls import reverse

from .models import Todo
# Create your views here.
@login_required(login_url='loginpage')
def home(request):
     if request.user.is_authenticated:
         form=CreateTodo()
         todos=Todo.objects.filter(user=request.user)
         return render(request, 'app/index.html',context={"form":form,"todos":todos})


def createtodo(request):
    if request.user.is_authenticated:
        user=request.user
        form=CreateTodo(request.POST)
        if form.is_valid():
         todo=form.save(commit=False)
         todo.user=user
         todo.save()
         print("Hello")
         return redirect('home')
    else:
        form=CreateTodo()
        return render(request, 'app/index.html',context={"form":form})

def deletetodo(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect('home')
# Ritik123@



def updatetodo(request,id):
    atodo=Todo.objects.all()
    todo=Todo.objects.get(id=id)
    form=CreateTodo(instance=todo)
    if request.method=='POST':
        form=CreateTodo(request.POST,instance=todo)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'app/update.html',context={"form":form,"todos":atodo})


def loginpage(request):
    if request.user.is_authenticated:
      return redirect('home')
    else:
     if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(request,username=username,password=password)
          print(user)
          if user is not None:
               login(request,user)
               return redirect('home')
          else:
              return render(request,'app/login.html') 
     else:     
       return render(request,'app/login.html')


def signup(request):
     if request.user.is_authenticated:
         return redirect('home')
     else:
      if request.method=='POST':  
          form=Createuser(request.POST)
        #   for field in form:
        #        print (field.name,field.errors)
          if form.is_valid():
               form.save()
               return redirect(reverse('loginpage'))
               
      form=Createuser()
      context={"form":form}
      return render(request, 'app/sign.html',context=context)
     
def logoutpage(request):
    logout(request)
    return redirect('home')

