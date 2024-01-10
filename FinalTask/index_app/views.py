
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid validations')
            return redirect('index_app:login')
    return render(request, 'loginpage.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if cpassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('index_app:register')
            else:
                 user = User.objects.create_user(username=username, password=password)
                 user.save()
                 return redirect('index_app:login')
        else:
             messages.info(request,"password not match")
             return redirect('index_app:register')
        return redirect('/')
    return render(request,'registerpage.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def form(request):
    return render(request,'register form.html')