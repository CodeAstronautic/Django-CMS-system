from django.db import models
from django.contrib.auth.models import AbstractUser
from Tap_admin.models import Project
class Enquiry(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_no = models.BigIntegerField()
    addres = models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    enquiry_date=models.DateTimeField(auto_now=True)
'''
class Blog_comment(models.Model):
    name=models.CharField(max_length=20)
    email = models.EmailField()
    comment=models.TextField()
    '''