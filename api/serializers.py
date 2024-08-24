from rest_framework import serializers
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from classes.models import Classes
from classperiod.models import ClassPeriod


class minimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields= ["full_name", "email"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'

class minimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields= ["full_name", "email"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'



class minimalClassesSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_class_name(self,object):
        return object.class_name
    class Meta:
        model=Classes
        fields= ["class_name"]

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classes
        fields='__all__'



class minimalCourseSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_course_name(self,object):
        return object.course_name
    class Meta:
        model=Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'


class minimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_first_name(self,object):
        return object.first_name
    class Meta:
        model=Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields='__all__'


class minimalClassPeriodSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_course(self,object):
        return object.course
    class Meta:
        model=Course

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassPeriod
        fields='__all__'



class minimalClassesSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_class_name(self,object):
        return object.class_name
    class Meta:
        model=Classes
        fields= ["class_name"]

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classes
        fields='__all__'



class minimalCourseSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_course_name(self,object):
        return object.course_name
    class Meta:
        model=Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'


class minimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_first_name(self,object):
        return object.first_name
    class Meta:
        model=Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields='__all__'


class minimalClassPeriodSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_course(self,object):
        return object.course
    class Meta:
        model=Course

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassPeriod
        fields='__all__'

