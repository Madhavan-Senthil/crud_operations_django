import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUD.settings')

import django
django.setup()

from CrudApp.models import *
from faker import Faker
from random import *
faker = Faker()
def generate (n):

    for i in range(n):
        fStudent_No= randint(1,1002)
        fStudent_Name= faker.name()
        fStudent_Class = randint(1,10)
        fStudent_Address = faker.city()
        Student_Record = Student.objects.get_or_create(Student_No=fStudent_No, Student_Name= fStudent_Name, Student_Class = fStudent_Class,Student_Address= fStudent_Address)
generate (10)