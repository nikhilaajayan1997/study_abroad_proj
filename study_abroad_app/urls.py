from django.urls import path
from study_abroad_app import views

urlpatterns=[
     path('home',views.home,name='home'),

     path('',views.home_page,name='home_page'),
     path('sign_up',views.sign_up,name='sign_up'),
     path('aboutus',views.aboutus,name='aboutus'),
     path('course',views.course,name='course'),
     path('contactus',views.contactus,name='contactus'),
     path('teacher',views.teacher,name='teacher'),
     path('course_detail',views.course_detail,name='course_detail'),




]