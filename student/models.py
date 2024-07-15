from django.db import models

class Students(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    student_code =models.SmallIntegerField()
    email=models.EmailField()
    age= models.SmallIntegerField()
    country= models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    date_of_birth= models.DateField()
    immediate_contact = models.CharField(max_length=20)
    bio = models.TextField()
    pic= models.ImageField()
    class_code = models.SmallIntegerField()
# Create your models here.


    def __str__(self):
        return f'{self.first_name}'
