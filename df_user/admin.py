from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("uname","upwd","uemail")
    search_fields = ("uname")



