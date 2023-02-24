from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User


# Create your models here.
class registermodel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,null=True)
    dob= models.DateField(null=True)
    email=models.EmailField()
    phone= models.CharField(max_length=50,null=True)
    username= models.CharField(max_length=150)
    password= models.CharField(max_length=150)

    """def __str__(self):
        return self.username """
    

class test(models.Model):
    t_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=13)
    t_amt=models.IntegerField(primary_key=False)
    preparation= models.CharField(max_length=100,null=True)
    sample= models.CharField(max_length=100)
    test_id= models.CharField(max_length=100,primary_key=True)

class package(models.Model):
    package_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=13)
    package_amt=models.IntegerField(primary_key=False)
    preparation= models.CharField(max_length=200)
    sample= models.CharField(max_length=200)
    package_id= models.CharField(max_length=100,primary_key=True)
    description= models.CharField(max_length=1000)
    #img=models.ImageField(upload_to='testbooking/packageimg',default="")


class adminmodel(models.Model):
    first_n=models.CharField(max_length=50)
    last_n=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    dob= models.DateField()
    email=models.EmailField()
    phone= models.CharField(max_length=50)
    id= models.CharField(max_length=150,primary_key=True)
    password= models.CharField(max_length=150)

"""class doctor(models.Model):
    qualification = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    loc = models.CharField(max_length=200)
    d_email=models.EmailField()
    d_phone=models.IntegerField()
    d_id= models.CharField(max_length=150,primary_key=True)
    d_name = models.ManyToManyField('docfullname')

class docfullname(models.Model):
    first_n = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)"""


"""class PatientList(models.Model):
    username = models.CharField(max_length=45,null=True)
    p_name = models.CharField(max_length=45,null=True)
    p_age = models.IntegerField(null=True)
    p_gender = models.CharField(max_length=45,null=True)

    """
    

class Patient_List(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,db_column='username',to_field='username')
    p_name = models.CharField(max_length=100)
    p_age = models.IntegerField()