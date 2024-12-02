from django.contrib import admin

# Register your models here.
from CrudApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list=['Student_No','Student_Name','Student_Class','Student_Address']


admin.site.register(Student,StudentAdmin)