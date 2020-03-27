from django import forms
from . models import Project,Document,MaterialType,material,Commercial,Residential,Sale
#from .  import 
#from .core.modeluploadss import Document
from django.forms import DateTimeField
from django.contrib.auth import get_user_model
User=get_user_model()


class DateInput(forms.DateInput):
    input_type='date'
class TimeInput(forms.DateInput):
    input_type='time'


class ProForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('project_type','project_name','address','sqfeet','project_desciption')
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )

class MaterialTypeForm(forms.ModelForm):
    class Meta:
        model = MaterialType
        fields='__all__'
class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = material
        fields='__all__'
        exclude=('project','bought_status','user','status')
        widgets={'purchased_date':DateInput()}

class CommercialForm(forms.ModelForm):
    class Meta:
        model = Commercial
        fields='__all__'
        exclude=('project',)
class ResidentialForm(forms.ModelForm):
    class Meta:
        model = Residential
        fields='__all__'
        exclude=('project',)


class saleimageForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields='__all__'
        exclude=('status','project')


class EditProfileAdminForm(forms.ModelForm):
     class Meta:
         model=User
         fields = ('first_name','last_name','phone_no','address','profile_pic')


