from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth import get_user_model
User=get_user_model()
from .form import EditProfileForm ,EnquiryForm
from django.contrib.auth.decorators import login_required

from Tap_admin.models import Project,Sale,Residential,Commercial

def index_page(request):
    return render(request,'customer/index.html') 
# Create your views here.

def register_user(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone_no=request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        try:
            User.object.get(username=email)
            return render(request,'customer/register.html',{'message':'email taken'})
        except:
            User.objects.create_user(phone_no=phone_no,address=address,is_user=True,last_name=lname,email=email,username=email,password=password,first_name=fname)
            return redirect(login_user)
    else:
        return render(request,'customer/register.html')
def login_user(request):
    
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        print(user)
        if user:
            login(request,user)
            #if request.user.is_user:
                #return render(request,'customer/index.html')
            return redirect(index_page)
        else:
            return render(request,'customer/login.html',{'message':'Invalid username or password'})
        
    else:
        return render(request,'customer/login.html',{'message':'Invalid username or password'}) 
    #else:       
       # return render(request,'customer/login.html')
  

def logout_user(request):
    logout(request)
    return redirect(login_user)
def edit_profile(request):
    pro=request.user
    if request.method=='POST':
        form =EditProfileForm(request.POST or None,instance=pro)
        if form.is_valid():
 
            form.save()
            return redirect('index')
        else:
            form =EditProfileForm(instance=pro)
            return render(request,'customer/edit.html',{'form':form,'pro':pro})
    else:
            form =EditProfileForm(instance=pro)
            return render(request,'customer/edit.html',{'form':form,'pro':pro})
def quotes(request):
    return render(request,'customer/quote.html')
def service_single(request):
    return render(request,'customer/service-single.html')
def vaastu(request):
    return render(request,'customer/vaastu.html')

def booking_flat(request):
    return render(request,'customer/booking_flat.html')
def blog_detail(request):
    return render(request,'customer/blog-details.html')
def contact(request):
    return render(request,'customer/contact.html')
def project_full_width(request):
    return render(request,'customer/project-full-width.html')
def project_view(request):
    projects=Sale.objects.filter(project__proj_sale_status='In Process')
    return render(request,'customer/all_project.html',{'projects':projects})

def project_three_column(request):
    return render(request,'customer/project-three-column.html')
def project_single(request,pk):
    project=Sale.objects.get(pk=pk)
    print(project.project.id)#.project.project_type)
    if project.project.project_type=='Residential':
        pro=Project.objects.get(id=project.project.id)
        detail=Residential.objects.get(project=project.project)
    else:
        pro=Project.objects.get(id=project.project.id)
        detail=Commercial.objects.get(project=pro)
    form = EnquiryForm()
    return render(request,'customer/project-single.html',{'project':project,'detail':detail,'form':form})

@login_required(login_url='/login/')
def enqiry_submit(request,id):
    pro=Project.objects.get(id=id)
    form=EnquiryForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form=form.save(commit=False)
            form.project=pro
            form.save()
    return redirect(project_view)


def home_01(request):
    return render(request,'customer/index.html')
def home_02(request):
    return render(request,'customer/index-2.html')
def project_grid_two_column(request):
    return render(request,'customer/project-grid-two-column.html')
def gallery(request):
    return render(request,'customer/gallery.html')


def Commercial_project(request):
    
    projects=Sale.objects.filter(project__proj_sale_status='In Process',project__project_type='Commercial')
    
    return render(request,'customer/all_project.html',{'projects':projects})
    
def Residential_project(request):
    projects=Sale.objects.filter(project__proj_sale_status='In Process',project__project_type='Residential')

    
    return render(request,'customer/all_project.html',{'projects':projects})
def view_project_detail(request):
    return redirect(project_single)
