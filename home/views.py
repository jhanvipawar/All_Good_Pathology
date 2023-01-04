from django.shortcuts import render, redirect, HttpResponse
from home.models import registermodel
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth

def register(request):  

    if request.method=="POST":
        FirstName=request.POST['FirstName']
        LastName=request.POST.get('LastName')
        email=request.POST.get('email')
        phone= request.POST.get('phone')
        username= request.POST.get('username')
        password= request.POST.get('password')
        repassword= request.POST.get('repassword')

        
        #regis=registermodel(first_name=FirstName,last_name=LastName,gender=gender,dob=dob,email=email,phone=phone,username=username,password=password)
        #regis.save() 

        if password==repassword:
            if FirstName.isalpha() and LastName.isalpha():
                if User.objects.filter(username=phone).exists():
                    messages.error(request, "phoen number already registered")
                    return render(request,'register.html')
                else:
                    user= User.objects.create_user(first_name=FirstName,last_name=LastName,email=email,username=phone,password=password)
                    user.save()

                    send_mail( FirstName +' '+ LastName +', here is your confirmation mail for registering at All Good Pathology', #subject
                    'Thank you, for chooisng All Good Pathology. We assure that your experience with us would be wonderful. All Good Pathology is the most trusted and well known pathology in your area.\n\nYou can use the username and password entered at the time of registration to log in into your account. We have wide range of tests and packages to satisfy your need.\n\n We hope you will get well soon. \n\n\n Our best wishes,\n All Good Pathology.',
                    'allgood.pathology@gmail.com', [email], )
                    
            else:
                messages.error(request, "first name and last name should be in letters")
                return render(request,'register.html')

            messages.success(request, "Your registration is now complete !!!")
            return render(request,'register.html')
        else:
            messages.error(request, "Password not matched")
            return render(request,'register.html')                    
       
    return render(request,'register.html')

def login_p(request):

    if request.method=="POST":
        login_phone=request.POST['login_phone']
        login_password=request.POST.get('login_password')
        
        user = auth.authenticate(username=login_phone,password=login_password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,"done")
            return render(request,'homepage.html')
        else:
            messages.error(request,"not done")
            return render(request,'login.html')

    return render(request,'login.html')

def logout_p(request):
    auth.logout(request)
    return render(request,'homepage.html')

def firstpage(request):
    return render(request,'homepage.html')

def homepage(request):
    return render(request,'homepage.html')
    
def profile(request):
    return render(request,'profile.html')

def test(request):
    return render(request,'test.html')    

def cart(request):
    return render(request,'cart.html')

def forgertpassword(request):
    return render(request,'forgetpassword.html')

def about(request):
    return render(request,'about.html')

def feedback(request):
    return render(request,'feedback.html')
