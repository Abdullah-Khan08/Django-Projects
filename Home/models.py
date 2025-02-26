from django.db import models

# Create your models here.
# i am creating schema here
class student(models.Model):
    #id=models.AutoField() ye django khud add kryga
    name= models.CharField(max_length=100)
    age=models.IntegerField(null=True ,blank=True)
    Dob=models.DateField(null=True ,blank=True)
    email=models.EmailField(null=True ,blank=True)
    address=models.TextField(null=True ,blank=True)
    image=models.ImageField(null=True ,blank=True)    