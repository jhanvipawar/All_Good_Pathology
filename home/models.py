from django.db import models
from django.contrib.auth.models import PermissionsMixin



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
