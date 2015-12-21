from django.contrib import admin
from .models import Teacher
from modelstudent import Student
from modelcourse import Course
class SignUpadmin(admin.ModelAdmin):
    class Meta:
        model=Teacher, Student, Course
admin.site.register(Teacher,Student,Course,SignUpadmin)

# Register your models here.
