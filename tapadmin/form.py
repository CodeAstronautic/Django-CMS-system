#from .models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
from .models import Enquiry

class EditProfileForm(forms.ModelForm):
     class Meta:
         model=User
         fields = ('first_name','last_name','address','phone_no')


class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields=('first_name','last_name','email','phone_no','addres')
        exclude =('project',)