from django.shortcuts import render,redirect
from . models  import ManagerProfile
from django.contrib.auth import get_user_model
User=get_user_model()
from Tap_admin.models import *
from . forms import *
from tapadmin.models import Enquiry
# Create your views here.
def index_page(request):
    return render(request,'manager1/index.html') 

def logout(request):
    return render(request,'manager1/logout.html')

def assigned_project(request):
    try:
        obj=ManagerProfile.objects.get(user=request.user)
        projects=Project.objects.filter(manager=obj)


    except:
        projects='No project Assigned'

    
    return render(request,'manager1/assigned.html',{'projects':projects})

def view_details(request,pk):
    obj=Project.objects.get(pk=pk)
    request.session['man_project']= obj.id
    return render(request,'manager1/details.html',{'data':obj})
def gallery(request,pk):
    obj=Project.objects.get(pk=pk)
    images=Document.objects.filter(project=obj)
    return render(request,'manager1/gallery.html',{'images':images})
def material_details(request,pk):
    obj=Project.objects.get(pk=pk)
    data=material.objects.filter(project=obj,bought_status='bought')
    request.session['man_project']= obj.id
    return render(request,'manager1/material.html',{'pk':pk,'data':data})

def material_request(request,pk):
    if request.method=='POST':
        form=MaterialRequestForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.project=Project.objects.get(pk=pk)
            form.user='manager'
            form.save()
            return redirect(material_details,pk)
    else:
        form=MaterialRequestForm()
        return render(request,'manager1/material_request.html',{'form':form,'pk':pk})


def material_request_status(request,pk):
    project=Project.objects.get(pk=pk)
    mat=material.objects.filter(project=project,user='manager')
    return render(request,'manager1/mat_reques_status.html',{'pk':pk,'mat':mat})

def add_material_man(request,pk,id):
    if request.method=='POST':
        mat=material.objects.get(id=id)
        form=MaterialForm(request.POST,instance=mat)
        if form.is_valid():
            form=form.save(commit=False)
            form.bought_status='bought'
            form.save()
            return redirect(material_details,pk)
        else:
            form=MaterialForm(request.POST,instance=mat)
            return render(request,'manager1/add_material.html',{'form':form,'pk':pk})

    else:
        mat=material.objects.get(id=id)
        project=mat.project
        form=MaterialForm(instance=mat)
        return render(request,'manager1/add_material.html',{'form':form,'pk':pk,'proj':project})

def project_enquiry(request,pk):
    enquiry=Enquiry.objects.filter(project__id=pk)
    request.session['man_project']=pk
    print(enquiry)  
    return render(request,'manager1/project_enquiry.html',{'enquiry':enquiry,'pk':pk})
def daily_report(request):
    if request.method=='POST':
        form=DailyReportForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.manager_name=request.user
            form.save()
            return redirect(index_page)


    form = DailyReportForm(request.user)
    return render(request,'manager1/daily_report.html',{'form':form})


def my_report(request):
    if request.method=='POST' and request.POST.get('pro') != 'Project':
        pro=request.POST.get('pro')
        p=Project.objects.get(id=pro)
        report=DailyReport.objects.filter(manager_name=request.user,project=p)

    else:
    #man=ManagerProfile.objects.get(user=request.user)
    
        report=DailyReport.objects.filter(manager_name=request.user)
    project=Project.objects.filter(manager__user=request.user)
    return render(request,'manager1/my_report.html',{'project':project,'report':report})
        
def edit_manager_profile(request):
    man=ManagerProfile.objects.get(user=request.user)
    
    if request.method=='POST':
        
        form =EditManagerProfileForm(request.POST,instance=man)
        if form.is_valid():
 
            form.save()
            return redirect(index_page)
        else:
            return render(request,'manager1/edit.html',{'form':form})
    else:
            man=ManagerProfile.objects.get(user=request.user)
            form =EditManagerProfileForm(instance=man)
            return render(request,'manager1/edit.html',{'form':form})

def profile_pic(request):
    form=EditProfilePicture()
    return render(request,'manager1/profile.html',{'form':form})
