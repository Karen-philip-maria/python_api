from rest_framework import serializers
from student.models import Students
from course.models import Course
from teacher.models import Teacher
# from class.models import Class
# from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Students
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields='__all__'

class classSerializer(serializers.ModelSerializer):
    class Meta:
        model= Class
        fields='__all__'

class classperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassPeriod
        fields='__all__'

