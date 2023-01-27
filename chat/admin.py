from django.contrib import admin
from .models import SignUpForm, Document,Room, Message, Registerinfo, Leaverequest

# Register your models here.

admin.site.register(SignUpForm)
admin.site.register(Document)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Registerinfo)
admin.site.register(Leaverequest)
