from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
User=get_user_model()
from . forms import EditProfileAdminForm,ProForm,DocumentForm,AddMaterialForm,MaterialTypeForm,ResidentialForm,CommercialForm,saleimageForm
from manager.models  import ManagerProfile,DailyReport
from . models import *
from tapadmin.models import Enquiry
#from Tap_admin.models import DailyReport
from manager.models import ManagerProfile
from django.db.models import Sum
# Create your views here.
def index_page(request):

    completed=Project.objects.filter(proj_sale_status='Completed').count()
    in_process=Project.objects.filter(proj_sale_status='in_process').count()

    not_started=Project.objects.filter(proj_sale_status='not_started').count()

    return render(request,'Tap_admin/index.html',{'completed':completed,'in_process':in_process,'not_started':not_started})

def login_user(request):
    if request.user.is_authenticated:
        if request.user.is_manager==True:
            return redirect('man_index')
        else:    
            return redirect(index_page)

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            if request.user.is_superuser:
                return render(request,'Tap_admin/index.html')
            elif request.user.is_manager:
                return render(request,'manager1/index.html')
        else:
            return render(request,'Tap_admin/login.html',{'message':'Invalid username or password'})        
    return render(request,'Tap_admin/login.html')
def logout_user(request):
    logout(request)
    return redirect(login_user)

def new_proj(request):
    if request.method=='POST':
        form=ProForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ongoing)
    form=ProForm()
    return render(request,'Tap_admin/New_project.html',{'form':form})

def ongoing(request):
    
    data=Project.objects.filter(proj_sale_status='Not Started')|Project.objects.filter(proj_sale_status='In Process')
    

    return render(request,'Tap_admin/ongoing.html',{'data':data})

def detail_project(request,pk):
    #select * from table where pk=pk
    obj=Project.objects.get(pk=pk)
    request.session['project_id']= obj.id
    return render(request,'Tap_admin/details.html',{'data':obj})
def delete_project(request,pk):
    obj=Project.objects.get(pk=pk)
    obj.delete()
    
    return redirect(ongoing)

def add_manager(request):
    if request.method=="POST":
        first_name=request.POST.get('Firstname')
        last_name=request.POST.get('lastname')
        address=request.POST.get('address')
        email=request.POST.get('emailid')
        phone_no=request.POST.get('mobileno')
        password=request.POST.get('password')
        gender=request.POST.get('gen')
        dob=request.POST.get('dob')
        pincode=request.POST.get('pincode')
        state=request.POST.get('State')
        city=request.POST.get('City')
        country=request.POST.get('Country')
       
        highest_degree=request.POST.get('Course')

        try:
            User.objects.get(email=email)
            return render(request,'Tap_admin/add_manager.html',{'message':'Email-id Taken'})
        except:
            u=User.objects.create_user(username=email,password=password,email=email,first_name=first_name,last_name=last_name,is_manager=True)
            ManagerProfile.objects.create(gender=gender,address=address,phone_no=phone_no,date_of_birth=dob,state=state,pincode=pincode,city=city,country=country,highest_degree=highest_degree,user=u)
            return redirect(manage_manager)
    else:

    
        return render(request,'Tap_admin/add_manager.html')


def management(request,pk):
    if request.method=='POST':
        man=request.POST['manager']
        print(man,'manager')
        obj=Project.objects.get(pk=pk)
        user=User.objects.get(email=man)
        manobj=ManagerProfile.objects.get(user=user)
        obj.manager=manobj
        obj.save()
        project=Project.objects.get(pk=pk)
        obj=ManagerProfile.objects.all()

        '''
        template_str='Tap_admin\mail.html'
        html_message = render_to_string(template_str,{'name':manobj.user.first_name,'project':project.project_name})
        print(project.project_name)
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        subject='New Project Assigned'
        to=manobj.user.email
        print(to)
        send_mail(subject,plain_message, email_from, [to] , html_message=html_message)
        '''

        return render(request,'Tap_admin/assign_manager.html',{'project':project,'obj':obj})
    else:
        project=Project.objects.get(pk=pk)
        obj=ManagerProfile.objects.all()

        return render(request,'Tap_admin/assign_manager.html',{'project':project,'obj':obj})
def manage_profile(request):

    return render(request,'Tap_admin/manage_profile.html')

#def edit_profile(request):
 #   return render(request,'Tap_admin/edit_profile.html')


def gallery(request,pk):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            pro=Project.objects.get(pk=pk)
            form.project=pro
            form.save()
            form = DocumentForm()
            pro=Project.objects.get(pk=pk)
            images=Document.objects.filter(project=pro)
            return render(request, 'Tap_admin/gallery.html', {'form': form,'images':images}) 
    else:    
        form = DocumentForm()
        pro=Project.objects.get(pk=pk)
        images=Document.objects.filter(project=pro)
        return render(request, 'Tap_admin/gallery.html', {'form': form,'images':images})
def delete_image(request,pk):
    data=Document.objects.get(pk=pk)
    id=data.project.id
    data.delete()
    return redirect(gallery,id)
'''
def send_mail(request):
    template_str='mail.html'
    html_message = render_to_string(template_str,{'name':'pooja'})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    subject='You have assigned one project '
    to='poojam9904@gmail.com'
    send_mail(subject,plain_message, email_from, [to] , html_message=html_message)
'''
def material_view(request,pk):
    obj=Project.objects.get(pk=pk)
    data=material.objects.filter(project=obj)
    total=material.objects.filter(project=obj).aggregate(Sum('cost'))
    return render(request, 'Tap_admin/material.html',{'data':data,'obj':obj,'total':total})

def add_material(request,pk):
    if request.method!='POST':
        obj=Project.objects.get(pk=pk)
        form=AddMaterialForm()
        return render(request,'Tap_admin/addMat.html',{'form':form,'obj':obj})
    else:
        form=AddMaterialForm(request.POST)
        obj=Project.objects.get(pk=pk)
        if form.is_valid():
            form=form.save(commit=False)
            form.project=obj
            form.user=request.user
            form.bought_status='bought'
            form.status='Approve'
            form.save()
            return redirect(material_view,pk)  
        #print(form.err)  
def add_material_type(request,pk):
    mat_type=MaterialType.objects.all()
    obj=Project.objects.get(pk=pk)
    if request.method!='POST':
        
        form=MaterialTypeForm()
        return render(request,'Tap_admin/addMatType.html',{'form':form,'obj':obj,'mat_type':mat_type})
    else:
        form=MaterialTypeForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'Tap_admin/addMatType.html',{'form':form,'obj':obj,'mat_type':mat_type})

def delete_mat_type(request,pk,id):
    mat_type=MaterialType.objects.get(id=pk)
    obj=Project.objects.get(id=id)
    mat_type.delete()
    return redirect(add_material_type,obj.id)


def sale(request,pk):
    pro=Project.objects.get(pk=pk)

    if request.method=='POST':

        try:
            sale=Sale.objects.get(project=pro)
            imageform=saleimageForm(request.POST, request.FILES,instance=sale)
            pro=Project.objects.get(pk=pk)

            if pro.project_type=='Residential':
                obj=Residential.objects.get(project=pro)
                form=ResidentialForm(request.POST,instance=obj)
            else:
                obj=Commercial.objects.get(project=pro)
                form=CommercialForm(request.POST,instance=obj)

        except:
            pro=Project.objects.get(pk=pk)

            if pro.project_type=='Residential':
                form=ResidentialForm(request.POST)
            else:
                form=CommercialForm(request.POST)

            imageform=saleimageForm(request.POST, request.FILES)    


        if form.is_valid() and imageform.is_valid():
            print("&&&")
            f=form.save(commit=False)
            f.project=pro
            f.save()
            im=imageform.save(commit=False)
            im.project=pro
            im.save()
            return redirect('sale',pk)
            
        else:
            print("B")
            imageform=saleimageForm()
            if pro.project_type=='Residential':
            #obj=Residential.objects.get()
                form=ResidentialForm(request.POST)
            else:
            #obj=Commercial.objects.get(project=pro)
                form=CommercialForm(request.POST)

            return render(request,'Tap_admin/sale.html',{'form':form,'imageform':imageform,'pk':pk})#,'update':update,'a':'no'})
    else:
        pro=Project.objects.get(pk=pk)
        try:
            print("try")
            sale=Sale.objects.get(project=pro)
            print("try")
            #res=Residential.objects.get(project=pro)
            if pro.project_type=='Residential':
                obj=Residential.objects.get(project=pro)
                form=ResidentialForm(instance=obj or None)
            else:

                obj=Commercial.objects.get(project=pro)
                print("try")
                form=CommercialForm(instance=obj or None)

            imageform=saleimageForm(instance=sale) 

            check='yes'
        except:
            imageform=saleimageForm()
            if pro.project_type=='Residential':
            #obj=Residential.objects.get()
                form=ResidentialForm()
            else:
            #obj=Commercial.objects.get(project=pro)
                form=CommercialForm()
            print("except")
            check='no'
        return render(request,'Tap_admin/sale.html',{'form':form,'imageform':imageform,'pk':pk,'a':check})#,'update':update,'a':'no'})


def update_sale(request,pk):
    status=request.POST.get('status')
    pro=Project.objects.get(pk=pk)
    pro.proj_sale_status='In Process'
    pro.save()
    s=Sale.objects.get(project=pro)
    s.status='Start'
    s.save()
    return redirect('details',pk)



def project_enquiry(request,pk):
    enquiry=Enquiry.objects.filter(project__id=pk)
    print(enquiry)

    return render(request,'Tap_admin/project_enquiry.html',{'enquiry':enquiry})
def new_enquiry(request):
    pro=Enquiry.objects.all()
    return render(request,'Tap_admin/new_enquiry.html',{'pro':pro})


def manage_manager(request):
    project=Project.objects.all()
    managers=ManagerProfile.objects.all()
    print(managers)
    return render(request,'Tap_admin/manage_manager.html',{'manager':managers,'project':project})


def delete_manager(request,pk):
    manager=ManagerProfile.objects.get(pk=pk)

    user=User.objects.get(id=manager.user.id)
    user.delete()
    #manager.delete()
    #user.delete()
    return redirect(manage_manager)

def edit_manager():
    pass
def manager_reporting(request):
    obj=DailyReport.objects.all().order_by('reporting_date')
    projects=Project.objects.all()
    manager=User.objects.filter(is_manager=True)

    if request.method=='POST':
        obj=DailyReport.objects.all().order_by('reporting_date')
        pro=request.POST.get('pro')
        man=request.POST.get('man')
        if man!='Manager':
            obj=DailyReport.objects.filter(manager_name=User.objects.get(id=man))

        if pro!='Project':
            obj=obj.filter(project=Project.objects.get(id=pro))
        
        

    return render(request,'Tap_admin/manager_reporting.html',{'reports':obj,'projects':projects,'manager':manager})


def edit_profile_admin(request):
    pro=request.user
    if request.method=='POST':
        form =EditProfileAdminForm(request.POST or None,request.FILES or None,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(edit_profile_admin)
        else:
            print("Error")
            form =EditProfileAdminForm(request.POST or None,request.FILES or None,instance=pro)
            return render(request,'Tap_admin/edit_profile.html',{'form':form,'pro':pro})
    else:
            form =EditProfileAdminForm(instance=pro)
            return render(request,'Tap_admin/edit_profile.html',{'form':form,'pro':pro})
    #return render(request,'Tap_admin/edit_profile.html')
