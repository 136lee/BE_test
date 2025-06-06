from django.shortcuts import render
from .models import *

# Create your views here.

def professor(request):
    professors=Professor.objects.all()
    return render(request, 'lectures/professor_list.html', {'professors':professors})

def student(request):
    students=Student.objects.all()
    lecture_student=LectureStudent.objects.all()
    return render(request, 'lectures/student_list.html', {'students':students, 'lecture_student':lecture_student})

def lecture(request):
    lectures=Lecture.objects.all()
    students=Student.objects.all()
    return render(request, 'lectures/lecture_list.html', {'lectures':lectures, 'students':students})

def index(request):
    return render(request, 'lectures/index.html')