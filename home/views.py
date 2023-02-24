from curses import OK
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from math import ceil
from .models import test,package,adminmodel,Patient_List,User





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
                    messages.error(request, "Phone number already registered",extra_tags='error')
                    return render(request,'register.html')
                else:
                    user= User.objects.create_user(first_name=FirstName,last_name=LastName,email=email,username=phone,password=password)
                    user.save()

                    #send_mail( FirstName +' '+ LastName +', here is your confirmation mail for registering at All Good Pathology', #subject
                    #'Thank you, for chooisng All Good Pathology. We assure that your experience with us would be wonderful. All Good Pathology is the most trusted and well known pathology in your area.\n\nYou can use the username and password entered at the time of registration to log in into your account. We have wide range of tests and packages to satisfy your need.\n\n We hope you will get well soon. \n\n\n Our best wishes,\n All Good Pathology.',
                    #'allgood.pathology@gmail.com', [email], )

            else:
                messages.error(request, "First name & Last name should be in letters",extra_tags='error')
                return render(request,'register.html')

            messages.success(request, "Your registration is now complete",extra_tags='success')
            return render(request,'register.html')
        else:
            messages.error(request, "Passwords not matched",extra_tags='error')
            return render(request,'register.html')

    return render(request,'register.html')

def login_p(request):

    if request.method=="POST":
        login_phone=request.POST.get('login_phone')
        login_password=request.POST.get('login_password')

        user = auth.authenticate(username=login_phone,password=login_password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, "YSuccessflly logged in !!!",extra_tags='success')
            #return render(request,'login.html')
            return redirect('http://127.0.0.1:8000/')


        else:
            messages.error(request,"Wrong phone number or password entered",extra_tags='error')
            return render(request,'login.html')

    return render(request,'login.html')

def logout_p(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/')

#def homepage(request):
    #return render(request,'homepage.html') http://127.0.0.1:8000/login

def firstpage(request):
    
    tests=test.objects.all()
    print(tests)
    n=len(tests)
    nslides=n//4 + ceil((n/4)-(n//4))
    test_d={'noof_slides':nslides,'range':range(1,nslides),'mytest':tests}

    packages=package.objects.all()
    print(packages)
    n=len(packages)
    nslides2=n//4 + ceil((n/4)-(n//4))
    package_d={'noof_slides':nslides2,'range':range(1,nslides2),'mypackage':packages}

    list_d={**test_d,**package_d}

    if request.method=="POST":
        tests=test.objects.all()
        packages=package.objects.all()

        testcha=request.POST.get('testcha_nav')
        packagecha_nav=request.POST.get('packagecha_nav')
        cart=request.session.get('cart')

        #test_id=test.objects.get(id=test_id)

        """if cart:
            quantity=cart.get(testcha)
            if quantity:
                cart[testcha]= quantity+ 1
            else:
                cart[testcha]= 1

        else:
            cart={}
            cart[testcha]=1"""

        request.session['cart']= cart
        print(testcha)
        return render(request,'homepage.html',list_d)

    return render(request,'homepage.html',list_d)


def register_a(request):
    if request.method=="POST":
        first_n=request.POST.get('first_n')
        last_n=request.POST.get('last_n')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        phone= request.POST.get('phone')
        id= request.POST.get('id')
        password= request.POST.get('password')
        repassword= request.POST.get('repassword')


        if password==repassword:
            if first_n.isalpha() and last_n.isalpha():
                if adminmodel.objects.filter(id=id).exists():
                    messages.error(request, "ID already registered",extra_tags='error')
                    return render(request,'register_a.html')
                else:
                    regis=adminmodel(first_n=first_n,last_n=last_n,gender=gender,dob=dob,email=email,phone=phone,id=id,password=password)
                    regis.save() 

            else:
                messages.error(request, "First name & Last name should be in letters",extra_tags='error')
                return render(request,'register_a.html')

            messages.success(request, "Your registration is now complete",extra_tags='success')
            return render(request,'register_a.html')
        else:
            messages.error(request, "Passwords not matched",extra_tags='error')
            return render(request,'register_a.html')                  
       
    return render(request,'register_a.html')

def login_a(request):
    if request.method=="POST":
        id=request.POST.get('id')
        password=request.POST.get('password')

        user = auth.authenticate(id=id,password=password)

        if user is not None:
            login(request, user)
            return render(request,'homepage.html')
        else:
            messages.error(request,"Wrong phone number or password entered",extra_tags='error')
            return render(request,'login_a.html')
    else:
        return render(request,'login_a.html')
    

def forgertpassword(request):
    return render(request,'forgetpassword.html')

def about(request):
    return render(request,'about.html')

def feedback(request):
    return render(request,'feedback.html')

def cart(request):
    return render(request,'cart.html')

"""def test_page(request):
    return render(request,'test_page.html')"""   

def testpage(request,id):
    tests=test.objects.filter(test_id=id)
    return render(request,'test_page.html',{'disptest':tests})

def packagepage(request,id):
    packages=package.objects.filter(package_id=id)
    return render(request,'package_page.html',{'disppackage':packages})

def profile(request):    

    if request.method=="POST":
        userchanav = request.user
        form = Patient_List(username=userchanav)


        form.p_name=request.POST.get('p_name')
        form.p_age=request.POST.get('p_age')
             #form.p_gender=request.POST.get('gender')



        if form.p_name.isalpha():
            if form.p_age.isnumeric():
                form.save()
                messages.success(request, "done bhai done",extra_tags='success')
                return render(request,'profile.html')
            else:
                messages.error(request, "Enter age in correct format",extra_tags='error')
                return render(request,'profile.html')
        else:
            messages.error(request, "Name should be in letters only",extra_tags='error')
            return render(request,'profile.html')     
             
        #username = User.objects.filter(userchename=username)
        #username = User.objects.get(username=user_all)

        #username_id=request.POST.get('username')
        #a=format(username_id)

        #user = request.user
        # form = Patient_List(user=user)
        form.save()
        
        #forenkey = Patient_List(username=request.user.username)
        
        #p_list=Patient_List(p_name=p_name,p_age=p_age,p_gender=p_gender,username=username)
        #p_list.save()

        #p_list=Patient_List.objects.create(p_name=p_name,p_age=p_age,p_gender=p_gender,username_id=user)

        
       
    return render(request,'profile.html')


    