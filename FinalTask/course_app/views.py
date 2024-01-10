from django.shortcuts import render

# Create your views here.
def cs(request):
    return render(request,'cs.html')
def comm(request):
    return render(request,'com.html')
def bio(request):
    return render(request,'bio.html')
def BE(request):
    return render(request,'BE.html')
def diploma(request):
    return render(request,'diploma.html')