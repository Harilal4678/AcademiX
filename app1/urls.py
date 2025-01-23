from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
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
    path('marks/',views.mark,name='mark'),
    path('mark_success/',views.mark_success,name='mark_success'),
    path('view_marks/',views.view_marks,name='view_marks'),
    path('send_message/', views.send_message, name='send_message'),
    path('notifications/', views.notifications, name='notifications'),
    path('view_student_marks',views.student_view_marks,name='student_view_marks'),
    path('send_assignment/', views.send_assignment, name='send_assignment'),
    path('view_assignment',views.view_assignment,name='view_assignment'),
    path('submit_assignment/<int:id>',views.submit_assignment,name='submit_assignment'),
    path('submit_assignment/Assignment_reply_save/<int:id>',views.Assignment_reply_save,name=' Assignment_reply_save'),
    path('teacher_view_assignments',views.teacher_view_assignments,name='teacher_view_assignments'),
    path('view_Assignment_reply/<int:id>',views.view_Assignment_reply,name='view_Assignment_reply'),
    path('staff_details_view',views.staff_details_view,name='staff_details_view'),
    path('lecture_profile/',views.lecture_profile,name='lecture_profile'),
    path('clerk_profile',views.clerk_profile,name='clerk_profile')





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)