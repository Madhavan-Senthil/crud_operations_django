from django.shortcuts import render
from CrudApp.models import Student
# Create your views here.



def select_view(request):
    student=Student.objects.all()
    return render(request,'CrudApp/index.html',{'student':student})