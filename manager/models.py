from django.db import models
from django.contrib.auth import get_user_model


from Tap_admin.models import Project
# Create your models here.

class ManagerProfile(models.Model):
    gen=(('Female','Female'),('Male','Male'))

    address=models.TextField()
    phone_no=models.BigIntegerField(null=False)
    gender=models.CharField(null=False,max_length=10,choices=gen)
    date_of_birth=models.DateField(null=False)
    
    state=models.CharField(null=False,max_length=20)
   
    pincode=models.IntegerField(null=False,default=395010)
    city=models.CharField(null=False,max_length=20,default="surat")
    country=models.CharField(null=False,max_length=20)
    highest_degree=models.TextField(null=False)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)


    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

class DailyReport(models.Model):
    manager_name=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='manager')
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    document = models.ImageField(upload_to='project/')
    remarks=models.TextField(null=False)
    reporting_date=models.DateField(auto_now=True)
    issues=models.TextField(null=True)