from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from . models import *
from django.utils import timezone

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
        elif staff.objects.filter(email=email,password=password).exists():
            userdetails=staff.objects.get(email=email, password=password)
            if  userdetails.password==request.POST['password']:
                request.session['stid']=userdetails.id
                request.session['stname']=userdetails.fullname
                request.session['password']=userdetails.password
                request.session['email']=userdetails.email
                request.session['gender']=userdetails.gender
                request.session['department']=userdetails.department
                request.session['stuser']='stuser'

                if userdetails.department == 'clerk':
                    return redirect('clerkdashboard')
                elif userdetails.department == 'lecturer':
                    return redirect('lecturedashboard')
                else:
                    return redirect('labassistantdashboard')
                
                
        else:
             return render(request,'index.html',{'status':'invalid email or password'})
            
def landingpage(request):
    return render(request,'landingpage.html')

def student_profile(request):
     user_id=request.session.get('sid')
     if user_id:
        vpro=studentdetails.objects.get(id=user_id)
     
     return render(request,'student_profile.html',{'result':vpro})
     
def logout(request):
     request.session.flush()
     response = redirect('index')  # Redirect to login page
     response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
     response['Pragma'] = 'no-cache'
     response['Expires'] = '0'
     return response

def staff_registration(request):
    if request.method == 'POST':
        fullname=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        department=request.POST.get('department')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        address=request.POST.get('address')

        registration=staff(
            fullname=fullname,
            email=email,
            phone=phone,
            gender=gender,
            department=department,
            password=password,
            image=image,
            address=address,
            


        )
        registration.save()



    return render(request,'staff_registration.html')



        
def stafflandingpage(request):
     return render(request,'stafflandingpage.html')

def clerkdashboard(request):
    return render(request,'clerkdashboard.html')

def lecturedashboard(request):
    return render(request,'lecturedashboard.html')

def labassistantdashboard(request):
    return render(request,'labassistantdashboard.html')
            



def mark_attendance(request):
    if request.method == 'POST':
        date = request.POST.get('date')  # Get the date of attendance
        status = None
        students = request.POST.getlist('students')  # List of selected student IDs
        for student_id in students:
            student = studentdetails.objects.get(id=student_id)
            # Fetch the attendance status for each student
            status = request.POST.get(f"status_{student_id}")  # Present or Absent
            # Create attendance record
            lecturer = staff.objects.get(id=request.session.get('stid'))  # The lecturer marking attendance
            
            attendance = Attendance(
                student=student,
                date=date,
                status=status,
                lecturer=lecturer,
            )
            attendance.save()

        return redirect('attendance_success')  # Redirect to a success page or back to dashboard

    # Get the list of students for the form
    students = studentdetails.objects.all()
    return render(request, 'attendance.html', {'students': students})

def attendance_success(request):
    return render(request, 'attendance_success.html')


def view_attendance(request):
    attendance = Attendance.objects.none()  # Default to an empty queryset

    if 'sid' in request.session:  # Example condition: student logged in
        student_id = request.session['sid']
        attendance = Attendance.objects.filter(student_id=student_id)
    else:
        attendance = Attendance.objects.all()  # Default to all attendance records if no condition is met

    return render(request, 'view_attendance.html', {'attendance': attendance})


