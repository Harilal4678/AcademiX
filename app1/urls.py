from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('registratin/',views.Registration,name='Registration'),
    path('login/',views.login,name='login'),
    path('landing/',views.landingpage,name='landingpage'),
    path('student_profile/',views.student_profile,name='student_profile'),
    path('logout/',views.logout,name='logout'),
    path('staff_registration/',views.staff_registration,name='staff_registration'),
    path('stafflandingpage/',views.stafflandingpage,name='stafflanding'),
    path('clerkdashboard/',views.clerkdashboard,name='clerkdashboard'),
    path('lecturedashboard/',views.lecturedashboard,name='lecturedashboard'),
    path('labassistantdashboard',views.labassistantdashboard,name='labassistantdashboard'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance_success/', views.attendance_success, name='attendance_success'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),


]