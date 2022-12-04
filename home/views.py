from django.shortcuts import render, redirect, HttpResponse
from home.models import registermodel
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def firstpage(request):

    return render(request,'homepage.html')
    
def patientprofile(request):
    return render(request,'patientprofile.html')

def test(request):
    return render(request,'test.html')    

def cart(request):
    return render(request,'cart.html')

def register(request):  

    if request.method=="POST":
        FirstName=request.POST['FirstName']
        LastName=request.POST.get('LastName')
        gender=request.POST.get('gender')
        dob= request.POST.get('dob')
        email=request.POST.get('email')
        phone= request.POST.get('phone')
        username= request.POST.get('username')
        password= request.POST.get('password')
        repassword= request.POST.get('repassword')

        if FirstName.isalpha() is not True:
            messages.error(request, 'only alphabets are allows')
            return render(request,'register.html')
            
        if LastName.isalpha() is not True:
            messages.error(request, 'only alphabets are allows')
            return render(request,'register.html')
        
        if password!=repassword:
            messages.error(request, 'password not matched')
            return render(request,'register.html')

        regis=registermodel(first_name=FirstName,last_name=LastName,gender=gender,dob=dob,email=email,phone=phone,username=username,password=password)
        regis.save() 

        send_mail(
            FirstName +' '+ LastName +', here is your confirmation mail for registering at All Good Pathology', #subject
            'Thank you, for chooisng All Good Pathology. We assure that your experience with us would be wonderful. All Good Pathology is the most trusted and well known pathology in your area.\n\nYou can use the username and password entered at the time of registration to log in into your account. We have wide range of tests and packages to satisfy your need.\n\n We hope you will get well soon. \n\n\n Our best wishes,\n All Good Pathology.',
            'allgood.pathology@gmail.com',
            [email],
        )

        messages.success(request, "Your registration is now complete !!!")
        return render(request,'register.html')
       
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

