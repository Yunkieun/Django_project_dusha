from django.contrib import admin


# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Member

admin.site.register(User, UserAdmin)

admin.site.register(Member)