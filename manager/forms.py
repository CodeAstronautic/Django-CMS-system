from django import forms

from Tap_admin.models import material,Project
from django.forms import DateTimeField
from manager.models import DailyReport,ManagerProfile
from django.contrib.auth import get_user_model
User=get_user_model()

class DateInput(forms.DateInput):
    input_type='date'
class TimeInput(forms.DateInput):
    input_type='time'


class MaterialRequestForm(forms.ModelForm):

    class Meta:
        model=material
        fields=('material_type','quantity','cost')

class MaterialForm(forms.ModelForm):
    class Meta:
        model=material
        fields=('material_type','quantity','cost','purchased_date','company_name')
        widgets={'purchased_date':DateInput()}

class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = ('project','document','remarks','issues')

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['project'].queryset=Project.objects.filter(manager__user=user)

class EditManagerProfileForm(forms.ModelForm):
     class Meta:
         model=ManagerProfile
         fields = ('address','phone_no','state','highest_degree','country','city','pincode')


class EditProfilePicture(forms.ModelForm):
    class Meta:
        model=User
        fields=('profile_pic',)