from django.urls import path
from . import views

urlpatterns = [
    path('student/register', views.student_register, name='student_register'),
    path('faculty/register', views.faculty_register, name='faculty_register'),
]
