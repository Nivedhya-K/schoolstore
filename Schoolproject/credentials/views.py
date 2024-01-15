from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import Courses
from .form import OrderForm
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('button.html')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info (request,'Username already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def button(request):
    return render(request,'button.html')

def order_confirm(request):
    if request.method == 'POST':
        message='Order Confirmed'
    return render(request,'order_confirm.html',{'message':message})
def form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
           # department_id = form.data['department_id']
            ##courses = Courses.objects.filter(department_id=department_id)
            #form.fields['course'].queryset = courses
            return order_confirm(request,"order_form.html")  # You can customize the success message here

    else:
        form = OrderForm()

    return render(request, 'form.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')
