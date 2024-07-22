from django.db import models

class Teacher(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    teacher_code =models.PositiveSmallIntegerField()
    email=models.EmailField()
    age= models.PositiveSmallIntegerField()
    country= models.CharField()
    phone_number = models.CharField()
    date_of_birth= models.DateField()
    immediate_contact = models.CharField(max_length=15)
    bio = models.TextField()

    def __str__ (self):
        return f"{self.first_name}{self.last_name}"
     





