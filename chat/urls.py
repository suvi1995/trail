from django.contrib import admin
from django.urls import path
from . import views
app_name = "fileapp"


urlpatterns = [
    path('', views.index, name='index'),
    path('leave', views.leave, name='leave'),
    path('std_leave', views.std_leave, name='std_leave'),
    path('stdinfo', views.stdinfo, name='stdinfo'),
    path('login_user', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('smain', views.smain, name='smain'),
    path('python/', views.python, name='python'),
    path('aws/', views.aws, name='aws'),
    path('web/', views.web, name='web'),
    path('devops/', views.devops, name='devops'),
    path('java/', views.java, name='java'),
    path('mainpg', views.mainpg, name='mainpg'),
    path('file_upload', views.file_upload, name='file_upload'),
    path('upload', views.send_files, name='uploads'),
    path('project', views.project, name='project'),
    path('home/', views.home, name='home'),
    path('stf_home/', views.stf_home, name='stf_home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')   
] 
