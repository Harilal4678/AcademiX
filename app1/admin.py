from django.contrib import admin

# Register your models here.
from .models import *

class studentdetailsadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','dob','gender','course','address','image','password')

admin.site.register(studentdetails,studentdetailsadmin)


class staffadmin(admin.ModelAdmin):
    list_display=('fullname','email','phone','gender','department','password','image','address')
admin.site.register(staff,staffadmin)

class Attendanceadmin(admin.ModelAdmin):
    list_display=('student','date','status','lecturer')
admin.site.register(Attendance,Attendanceadmin)

class marksadmin(admin.ModelAdmin):
    list_display=('student','physics','maths','computer_science')
admin.site.register(marks,marksadmin)

class notificationadmin(admin.ModelAdmin):
    list_display=('sender','recipient','message','timestamp','is_read')
admin.site.register(Notification,notificationadmin)

class Assignmentsadmin(admin.ModelAdmin):
    list_display=('teacher','student','title','description','due_date','created_at')
admin.site.register(Assignments,Assignmentsadmin)

class AssignmentAnswersAdmin(admin.ModelAdmin):
    list_display=('assignment','student','text_answer','file_answer','submitted_at')
admin.site.register(AssignmentAnswers,AssignmentAnswersAdmin)