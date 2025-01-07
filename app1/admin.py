from django.contrib import admin

# Register your models here.
from .models import studentdetails

class studentdetailsadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','dob','gender','course','address','image','password')

admin.site.register(studentdetails,studentdetailsadmin)
