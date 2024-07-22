from rest_framework import serializers
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from classes.models import Classes
from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classes
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields='__all__'



class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassPeriod
        fields='__all__'
