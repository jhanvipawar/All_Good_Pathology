from django.db import models

# Create your models here.
class registermodel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob= models.DateField(null=True)
    email=models.EmailField()
    phone= models.CharField(max_length=10)
    username= models.CharField(max_length=150)
    password= models.CharField(max_length=150)

    """def __str__(self):
        return self.username """