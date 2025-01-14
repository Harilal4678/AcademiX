from django.contrib import admin

# Register your models here.
from .models import *

class studentdetailsadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','dob','gender','course','address','image','password')

admin.site.register(studentdetails,studentdetailsadmin)


class staffadmin(admin.ModelAdmin):
    list_display=('fullname','email','phone','gender','department','password','image','address')
admin.site.register(staff,staffadmin)