from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class SignUpForm(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password1 = models.CharField(max_length=1000)
    password2 = models.CharField(max_length=1000)
    us =models.CharField(max_length=1000)
    def __str__(self):
        return self.username
  
class Document(models.Model):
    
    title=models.CharField(max_length=100)
    document=models.FileField(upload_to="")
    def __str__(self):
        return self.title
class Registerinfo(models.Model):
    
    first_name= models.CharField(max_length=1000)
    last_name= models.CharField(max_length=1000)
    dob = models.CharField(max_length=1000)
    gender = models.CharField(max_length=1000)
    mail = models.CharField(max_length=1000)
    mobile_number = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    def __str__(self):
        return self.first_name
class Leaverequest(models.Model):
    Name= models.CharField(max_length=1000)
    TO = models.CharField(max_length=1000)
    Date = models.CharField(max_length=1000)
    Reason = models.CharField(max_length=10000)
    def __str__(self):
        return self.Name
class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

