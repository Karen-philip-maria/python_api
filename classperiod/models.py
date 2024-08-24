from django.db import models



# from course.models import Course

# from student.models import Student



class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course= models.CharField(max_length=20)
    classroom= models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=10)

    # course = models.ManyToManyField(Course)
    # teacher = models.ManyToManyField(Student)


    def __str__(self):
        return f"{self.course} {self.day_of_week}"

# Create your models here.
