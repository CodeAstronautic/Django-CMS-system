from django.db import models
from django.contrib.auth.models import AbstractUser
#from Tap_admin.models import Project
#from django.contrib.auth import get_user_model
#from manager import models
# Create your models here.
class User(AbstractUser):
    is_admin=models.BooleanField('Is admin',default=False)
    is_manager=models.BooleanField('Is manager',default=False)
    is_user=models.BooleanField('Is user',default=True)
    is_sales=models.BooleanField('Is sales',default=False)
    address=models.TextField(default=True)
    phone_no=models.BigIntegerField(null=True)
    profile_pic=models.ImageField(null=True)

class Project(models.Model):
    proj_status=(
        ('Completed','Completed'),
        ('In Process','In Process'),
        ('Not Started','Not Started')

 
   )
    proj_type=(
        ('Residential','Residential'),
        ('Commercial','Commercial'),
    
    )
    project_type=models.CharField(max_length=20,choices=proj_type)
    project_name=models.CharField(max_length=50)
    address=models.TextField()
    sqfeet=models.DecimalField(null=False,max_digits=10,decimal_places=5)
    proj_sale_status=models.CharField(max_length=15,choices=proj_status,default='Not Started')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    manager=models.ForeignKey('manager.ManagerProfile',on_delete=models.CASCADE,null=True)
    project_desciption=models.TextField(null=True)
    def __str__(self):
        return self.project_name

class Document(models.Model):
    document = models.ImageField(upload_to='project/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
'''
photo
imageField
Project--foreignkey
'''

class MaterialType(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class material(models.Model):
    material_type=models.ForeignKey(MaterialType,on_delete=models.CASCADE,null=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    cost=models.IntegerField()
    quantity=models.IntegerField()
    purchased_date=models.DateField(null=True)
    company_name=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=20,choices=(('Pending','Pending'),('Approve','Approve'),('Reject','Reject')),default='Pending')
    bought_status=models.CharField(max_length=30,default='Not bought')
    user=models.CharField(max_length=20,default='admin')


class Sale(models.Model):
    status=models.CharField(max_length=10,default='No')
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='property image/',null=True)
    image2=models.ImageField(upload_to='property image/',null=True)
    image3=models.ImageField(upload_to='property image/',null=True)
    
class Commercial(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    no_of_floor=models.IntegerField()
    no_of_office=models.IntegerField()


class Residential(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    no_of_building=models.IntegerField()
    no_of_floor=models.IntegerField()
    
    no_of_1bhk=models.IntegerField()
    no_of_2bhk=models.IntegerField()
    no_of_3bhk=models.IntegerField()
    no_of_4bhk=models.IntegerField()


'''
class Book(models.Model):
'''