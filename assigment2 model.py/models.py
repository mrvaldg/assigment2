from __future__ import unicode_literals
from django.db import models

class Teacher(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    office_details=models.CharField(max_length=120,null=True,blank=True)
    phone=models.PositiveIntegerField(max_length=120,null=True,blank=True)
    email=models.EmailField(max_length=120,null=True)
    def __unicode__(self):
        return self.firstname,self.lastname


class Course(models.Model):
    name=models.CharField(max_length=120)
    code=models.CharField(max_length=120)
    classromm=models.CharField(max_length=120)
    times=models.DateTimeField(max_length=120)
    teacher=models.OneToOneField(Teacher)
    studenten=models.ManyToManyField(Student)
    def __unicode__(self):
        return self.name


class Student(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    email=models.EmailField(max_length=120,null=True,blank=True)
    courses=models.ManyToManyField(Course)
    def __unicode__(self):
        return self.firstname,self.lastname


# Create your models here.
