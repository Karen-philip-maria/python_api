from django.db import models

from course.models import Course

class Student(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    student_code =models.PositiveSmallIntegerField()
    email=models.EmailField()
    age= models.PositiveSmallIntegerField()
    country= models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    date_of_birth= models.DateField()
    immediate_contact = models.CharField(max_length=20)
    class_code = models.PositiveSmallIntegerField()

    courses = models.ManyToManyField(Course)

# Create your models here.


    def __str__(self):
        return f"{self.first_name}{self.last_name}"

