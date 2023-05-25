from django.shortcuts import render
from django.http import HttpResponse
from Main.models import Student
from django import forms

genderChoices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

levelChoices = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

statuses = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
]

class addStudentForm(forms.Form):
    name = forms.CharField(label='Name')
    id = forms.CharField(label='studentId')
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='DOB')
    email = forms.CharField(label='studentEmail')
    gpa = forms.CharField(label='studentGpa')
    level = forms.ChoiceField(label='studentLevel', choices=levelChoices)
    status = forms.ChoiceField(label='studentStatus', choices=statuses)
    phone = forms.CharField(label='studentPhone')
    department = forms.CharField(label='studentDep')
    gender = forms.ChoiceField(label='studentGender', choices=genderChoices)

# Create your views here.
def index(request):
    return render(request, "index/index.html") 

def edit(request):
    return render(request, 'editStudent/Edit_Student.html')

def home(request):
    return render(request, 'home/home.html')

def addStudent(request):
    return render(request, "addStudent/add_student.html",{
        'form': addStudentForm()
    })

def formSubmission(request):
    if request.method == 'POST':
        t_name = request.POST['name']
        t_gender = request.POST['gender']
        t_gpa = request.POST['gpa']
        t_id = request.POST['id']
        t_level = request.POST['level']
        t_status = request.POST['status']
        t_DOB = request.POST['DOB']
        t_dep = request.POST['department']
        t_email = request.POST['email']
        t_phone = request.POST['phone']

        temp = Student(name=t_name, gender=t_gender, gpa=t_gpa, id=t_id, level=t_level, status=t_status, dateOfBirth=t_DOB, 
                       department=t_dep, email=t_email, phone=t_phone)
        
        temp.save()
        return HttpResponse("Data saved!")
