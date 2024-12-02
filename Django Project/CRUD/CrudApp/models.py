from django.db import models

# Create your models here.
class Student(models.Model):
    Student_No=models.IntegerField()
    Student_Name=models.CharField(max_length=50)
    Student_Class=models.IntegerField()
    Student_Address=models.CharField(max_length=50)
