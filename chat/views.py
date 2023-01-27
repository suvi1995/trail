from django.shortcuts import render, redirect, redirect,HttpResponseRedirect,HttpResponse
from .models import SignUpForm, Document, Room, Message,Registerinfo, Leaverequest
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import UploadForm
from django.http import JsonResponse
import os
# Create your views here. 





def index(request):
    if request.method=='POST':
        global username
        username = request.POST['uname']
        email = request.POST['mail']
        password = request.POST['pwd1']
        conform_password = request.POST['pwd2']
        ust= request.POST['us']
        if password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Email alreay exit')
                return HttpResponseRedirect("/")
            if ust== "Staff":
                user=User.objects.create_superuser(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                sign = SignUpForm(username=username, email=email, password1=password, password2=conform_password, us=ust)
                sign.save()
                return HttpResponseRedirect("login_user")
            elif ust == "Student":
                user=User.objects.create_user(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                sign = SignUpForm(username=username, email=email, password1=password, password2=conform_password, us=ust)
                sign.save()
                return HttpResponseRedirect("login_user")
            else:
                messages.info(request, 'Please Select User Type')
                return HttpResponseRedirect("/")
        else:
            messages.info(request, 'Password and confirm password mismatch')
            return HttpResponseRedirect("/")       
    else:
        return render(request, 'signup.html')
def login_user(request):
    if request.method == "POST":
        username= request.POST['uname']
        psw= request.POST['pssword']
        user=authenticate(username=username, password=psw)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect("smain")
            elif user is not None:
                return HttpResponseRedirect("mainpg")
        else:
            messages.info(request, 'Incorrect username and password')
            return HttpResponseRedirect("login_user")
    return render(request, 'login.html')
def mainpg(request):
    return render(request, 'mainpg.html')
def python(request):
    return render(request, 'python.html')
def aws(request):
    return render(request, 'AWS.html')
def devops(request):
    return render(request, 'devops.html')
def java(request):
    return render(request, 'Java.html')
def web(request):
    return render(request, 'web angular.html')
def smain(request):
    return render(request, 'stf_mainpg.html')

def register(request):
    if request.method == "POST":
        global fname
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        gen = request.POST['gen']
        eid = request.POST['eid']
        mno = request.POST['mno']
        course= request.POST['course']
        if Registerinfo.objects.filter(first_name=fname,last_name=lname, dob=dob, gender=gen, mail=eid, mobile_number=mno, course=course).exists():
            messages.info(request, "Details registered already")
            return HttpResponseRedirect("register")
        else:
            queryset=Registerinfo.objects.filter(first_name=fname).delete()
            reg= Registerinfo.objects.create(first_name=fname, last_name=lname, dob=dob, gender=gen, mail=eid, mobile_number=mno, course=course)
            reg.save()
            messages.success(request, 'Registered successfully')
    return render(request, 'register.html')

    return render(request,"base.html",{'all':queryset, 't':tit})

def stdinfo(request):
    tit = "Student Details"
    queryset = Registerinfo.objects.all()
    return render(request, 'studentinfo.html',{'all':queryset, 't':tit})
def file_upload(request):
    return render(request, 'upload_task.html')
def leave(request):
    if request.method == "POST":
        name = request.POST['sender']
        to = request.POST['mai']
        date = request.POST['date']
        reason = request.POST['reason']
        leave = Leaverequest(Name=name, TO=to, Date=date, Reason=reason)
        leave.save()
        messages.info(request,"Leave details submitted successfully")
        return HttpResponseRedirect("leave")
    return render(request,'leave.html')
def std_leave(request):
    tit = "Leave Details"
    queryset = Leaverequest.objects.all()
    return render(request, 'leavestatus.html',{'all':queryset, 't':tit})

def send_files(request):
    if request.method == "POST":
        title=request.POST.get('title')
        myfile = request.FILES.getlist('uploadfiles')
        exist = Document.objects.filter(document=myfile).exists()
        if exist:
            messages.info(request, "The file is already exist")
        else:
            for f in myfile:
                doc=Document(title=title, document = f).save()
                messages.info(request, 'File uploaded successfully')
                return HttpResponseRedirect("file_upload")
def project(request):
    tit = "Task/project Details"
    queryset = Document.objects.all()
    return render(request, 'viewupload.html',{'all':queryset, 't':tit})
    
    return render(request, 'leavereq.html')
def home(request):
    return render(request, 'query.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
def stf_home(request):
    return render(request, 'stf_query.html')


