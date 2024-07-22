from django.db import models

class Classes(models.Model):
    class_name = models.CharField()
    class_capacity = models.PositiveSmallIntegerField()
    class_duration = models.DateField()
    class_training_assistant= models.TextField()
    class_representatives= models.TextField()
    class_empty_slots= models.PositiveSmallIntegerField()
    class_white_boards= models.PositiveSmallIntegerField()
    class_number_of_tvs= models.PositiveSmallIntegerField()
    class_number_of_desks= models.PositiveSmallIntegerField()
    class_number_of_chairs= models.PositiveSmallIntegerField()
    class_code= models.PositiveSmallIntegerField()


    def __str__(self):
        return f"{self.class_name}{self.class_capacity}"
