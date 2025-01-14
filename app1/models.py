from django.db import models

class studentdetails(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    dob=models.DateField(max_length=30)
    gender=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    image=models.ImageField(upload_to='student_user')
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
    
class staff(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    gender=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    image=models.ImageField(upload_to='student_user')
    address=models.CharField(max_length=30)

    
    def __str__(self):
        return self.fullname
   
