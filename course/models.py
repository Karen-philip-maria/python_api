from django.db import models

# from student.models import Student

class Course(models.Model):
    course_title= models.CharField()
    course_category= models.CharField()
    course_start_date= models.DateField()
    course_end_date = models.DateField()
    course_code =models.PositiveSmallIntegerField()
    teacher_code= models.PositiveSmallIntegerField()
    course_attendees= models.CharField()


    # student = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.course_title}{self.course_category}"

