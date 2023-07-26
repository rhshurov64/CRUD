from django.contrib import admin
from .models import AddUser

# Register your models here.
@admin.register(AddUser)

class AddUserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email','age')