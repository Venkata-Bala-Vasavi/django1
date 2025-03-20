from django.shortcuts import render,HttpResponse,redirect
from .models import Student
from django.contrib import messages
from faker import Faker
fake=Faker()
def add_student(request):
    student=Student(
        name=fake.name(),
        age=fake.random_int(min=18,max=30),
        email=fake.email()
    )
    student.save()
    redirect('student_list')
    return HttpResponse("Student record added successfully")
def student_list(request):
    students=Student.objects.all()
    return render(request,'modelapp/index.html',{'students':students})
