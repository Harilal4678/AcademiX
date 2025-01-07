from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('registratin/',views.Registration,name='Registration'),
    path('login/',views.login,name='login'),
    path('landing/',views.landingpage,name='landingpage')
]