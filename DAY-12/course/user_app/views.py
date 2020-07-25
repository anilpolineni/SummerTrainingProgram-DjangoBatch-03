from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegisterForm, FacultyRegisterForm
from .models import StudentRegister
from django.core.mail import EmailMessage
from course import settings

# Create your views here.

def student_register(request):
    form = StudentRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            student = StudentRegister(name=request.POST.get('name'),
                                      email=request.POST.get('email'),
                                      phone=request.POST.get('phone'),
                                      age=request.POST.get('age'),
                                      gender=request.POST.get('gender'),
                                      dob=request.POST.get('dob'))
            student.save()
            # name = request.POST.get('name')
            name = form.data['name']
            receiver = form.data['email']
            sub = 'course registration'
            body = 'Hi '+name.title+" Your course registration has been done " \
                              "successfully!!"
            sender = settings.EMAIL_HOST_USER

            email_mgs = EmailMessage(sub, body, sender, [receiver])
            email_mgs.send()
            return HttpResponse("student register done!!!")
    return render(request, 'user/student_register.html', {'form':form})


def faculty_register(request):
    form = FacultyRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('Faculty added!!')
    return render(request, 'user/faculty_register.html', {'form': form})
