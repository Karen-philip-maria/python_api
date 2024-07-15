from django.db import models
class Class(models.Model):
    class_name = models.CharField()
    class_capacity = models.SmallIntegerField()
    class_duration = models.DateField()
    class_training_assistant= models.TextField()
    class_representatives= models.TextField()
    class_empty_slots= models.SmallIntegerField()
    class_white_boards= models.SmallIntegerField()
    class_number_of_tvs= models.SmallIntegerField()
    class_number_of_desks= models.SmallIntegerField()
    class_number_of_chairs= models.SmallIntegerField()
    class_code= models.SmallIntegerField()

# Create your models here.
