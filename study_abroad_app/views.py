from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def home(request):
    return render(request,'login.html')

def sign_up(request):
    return render(request,'sign_up.html')

def aboutus(request):
    return render(request,'aboutus.html')

def course(request):
    return render(request,'course.html')
    
def contactus(request):
    return render(request,'contact.html')

def teacher(request):
    return render(request,'teacher.html')

def course_detail(request):
    return render(request,'course_detail.html')

