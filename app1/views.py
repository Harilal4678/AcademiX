from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . models import *
from django.utils import timezone
from django.utils.timezone import now

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
    student_id=request.session.get('sid')
    assignments=Assignments.objects.filter(id=student_id)

    context = {
        'assignment': assignments.first() if assignments.exists() else None,  # Get the first assignment or None
    }
    return render(request, 'landingpage.html', context)

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


    
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    # Filter attendance records by date range
    if from_date and to_date:
        attendance = Attendance.objects.filter(date__range=[from_date, to_date])
    else:
        attendance = Attendance.objects.all()

    context = {
        'attendance': attendance
    }
    return render(request, 'view_attendance.html', context)



    # return render(request, 'view_attendance.html', {'attendance': attendance})

def mark(request):
    if request.method == 'POST':
        students=request.POST.getlist('students')
        for student_id in students:
            student=studentdetails.objects.get(id=student_id) 
            physics=request.POST.get(f"physics_{student_id}") 
            maths=request.POST.get(f"maths_{student_id}")          
            computer_science=request.POST.get(f"computer_science_{student_id}")  
            exam_type=request.POST.get('exam_type')
            mark=marks(
                student=student,
                physics=physics,
                maths=maths,
                computer_science=computer_science,
                exam_type=exam_type
            )
            mark.save()
        return redirect('mark_success')
    students = studentdetails.objects.all()
    return render(request, 'marks.html', {'students': students})

def mark_success(request):
    return render(request,'mark_success.html')

def view_marks(request):
    mark=marks.objects.none()
    if 'sid' in request.session:  # Example condition: student logged in
        student_id = request.session['sid']
        mark = marks.objects.filter(student_id=student_id)
    else:
        mark=marks.objects.all()

    
    return render(request,'view_marks.html',{'mark':mark})




def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        recipient_type = request.POST.get('recipient')  # student, staff, or department-specific
        sender = staff.objects.get(id=request.session.get('stid'))  # Current clerk

        if recipient_type == 'student':
            # Notify all students
            students = studentdetails.objects.all()
            for student in students:
                Notification.objects.create(sender=sender, recipient='student', message=message)

        elif recipient_type == 'lab_assistants':
            # Notify all Lab Assistants
            lab_assistants = staff.objects.filter(department='Lab Assistant')
            for assistant in lab_assistants:
                Notification.objects.create(sender=sender, recipient='staff', message=message)

        elif recipient_type == 'lecturers':
            # Notify all Lecturers
            lecturers = staff.objects.filter(department='Lecturer')
            for lecturer in lecturers:
                Notification.objects.create(sender=sender, recipient='staff', message=message)

        elif recipient_type == 'clerks':
            # Notify all Clerks
            clerks = staff.objects.filter(department='Clerk')
            for clerk in clerks:
                Notification.objects.create(sender=sender, recipient='staff', message=message)

        elif recipient_type == 'all':
            # Notify all students and staff
            students = studentdetails.objects.all()
            staffs = staff.objects.all()
            for student in students:
                Notification.objects.create(sender=sender, recipient='student', message=message)
            for staff_member in staffs:
                Notification.objects.create(sender=sender, recipient='staff', message=message)

        return redirect('clerkdashboard')  # Redirect to the clerk dashboard after sending the message

    return render(request, 'send_message.html')




def notifications(request):
    user_type = None
    notifications = []

    if 'sid' in request.session:  # Student
        user_type = 'student'
    elif 'stid' in request.session:  # Staff
        user_type = 'staff'

    if user_type:
        notifications = Notification.objects.filter(recipient=user_type).order_by('-timestamp')

    return render(request, 'notifications.html', {'notifications': notifications})


def student_view_marks(request):
    student_id=request.session.get('sid')
    if not student_id:
        return render(request,'error.html')
    student=studentdetails.objects.get(id=student_id)
    student_marks=marks.objects.filter(student=student)
    return render(request,'student_view_marks.html',{'marks':student_marks})

def send_assignment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        student_id = request.POST.get('student')
        due_date = request.POST.get('due_date')

        # Get the logged-in teacher (staff with lecturer department) and selected student
        teacher = staff.objects.get(id=request.session['stid'])  # Assumes staff is logged in
        if teacher.department != 'lecturer':  # Check if the staff belongs to the lecturer department
            return redirect('home')  # Or handle with an appropriate response

        student = studentdetails.objects.get(id=student_id)

        # Create a new assignment
        Assignments.objects.create(
            teacher=teacher,
            student=student,
            title=title,
            description=description,
            due_date=due_date,
            created_at=timezone.now(),  # Using timezone.now()
        )
        return redirect('lecturedashboard')  # Redirect after successful submission

    students = studentdetails.objects.all()
    context = {
        'students': students,
        'created_at': timezone.now(),  # Using timezone.now()
    }
    return render(request, 'send_assignment.html', context)


def view_assignment(request):
    tem=request.session.get('sid')
    student=studentdetails.objects.get(id=tem)
    assignment=Assignments.objects.get(student=student)

    return render(request,'view_assignment.html',{'assignment':assignment})

def submit_assignment(request,id):
    tem=request.session['sid']
    vpro=studentdetails.objects.get(id=tem)
    xpro=Assignments.objects.get(id=id)
    return render(request,'submit_assignment.html',{'result':vpro, 'res':xpro})

def Assignment_reply_save(request,id):
    tem=request.session['sid']
    if request.method =='POST':
        Assignment_instance=Assignments.objects.get(id=id)
        student_instance=studentdetails.objects.get(id=tem)
        content=request.POST.get('content')
        
        file = request.FILES.get('file') 
        fs = FileSystemStorage()
        image_path = fs.save(file.name, file)


        # message_save = AssignmentAnswers(assignment=Assignment_instance,student=student_instance,text_answer=content,file_answer=file)
        # message_save.save()

        answer,created=AssignmentAnswers.objects.update_or_create(
            assignment=Assignment_instance,
            student=student_instance,
            defaults={
                'text_answer':content,
                'file_answer':file

            }


        )
        if created:
            return render(request,'assignment_success.html',{'result':'created_new'})
        else:
            return render(request,'assignment_success.html',{'result':'update_existing'})
    return render(request,'assignment_success.html')

def teacher_view_assignments(request):
    teacher=request.session.get('stid')
    assignment=Assignments.objects.filter(teacher=teacher)
    return render(request,'teacher_view_assignments.html',{'res':assignment})

def view_Assignment_reply(request,id):
    try:
        assignment_answer=AssignmentAnswers.objects.get(assignment=id) #yes we actually need get instead of filter but for me in the template there is condition checking so get returns error if nothing to fetch but filter returns none so i can do if condition and show nothing if nothing to show instead of error
    except AssignmentAnswers.DoesNotExist:
        assignment_answer=None
    return render(request,'view_Assignment_reply.html',{'result':assignment_answer})









