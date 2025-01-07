from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from . models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def Registration(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        course=request.POST.get('Course')
        address=request.POST.get('address')
        image=request.FILES.get('image')
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')

        registration=studentdetails(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            dob=dob,
            gender=gender,
            course=course,
            address=address,
            image=image,
            password=password


        )
        registration.save()

    return render(request,'Registration.html')


def login(request):
        email=request.POST.get('email')
        password=request.POST.get('password')

        if studentdetails.objects.filter(email=email,password=password).exists():
            userdetails=studentdetails.objects.get(email=email, password=password)
            if  userdetails.password==request.POST['password']:
                request.session['sid']=userdetails.id
                request.session['sname']=userdetails.first_name
                request.session['password']=userdetails.password
                request.session['email']=userdetails.email
                request.session['gender']=userdetails.gender
                request.session['course']=userdetails.course
                request.session['suser']='suser'
                
                return render(request,'landingpage.html')
        else:
             return render(request,'index.html',{'status':'invalid email or password'})
            
def landingpage(request):
    return render(request,'landingpage.html')