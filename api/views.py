from django.shortcuts import render

from rest_framework.views import APIView

from student.models import Students
from .serializers import StudentSerializer

from classes.models import Class
from .serializers import ClassSerializer

from classperiod.models import ClassPeriod
from .serializers import classperiodSerializer


from course.models import Course
from .serializers import CourseSerializer

from teacher.models import Teacher
from .serializers import TeacherSerializer

from rest_framework.response import Response

class StudentListView(APIView):
    def get (self, request):
        student = Students.objects.all()
        serializer = StudentSerializer(student, many= True)
        return Response(serializer.data)
    


class ClassPeriodListView(APIView):
    def get (self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = classperiodSerializer(classperiod, many= True)
        return Response(serializer.data)



class TeacherListView(APIView):
    def get (self, request):
        teacher = Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many= True)
        return Response(serializer.data)
    



class CourseListView(APIView):
    def get (self, request):
        course = Course.objects.all()
        serializer=CourseSerializer(course, many= True)
        return Response(serializer.data)
    


class ClassListView(APIView):
    def get (self, request):
        classes= Class.objects.all()
        serializer=ClassSerializer(classes, many= True)
        return Response(serializer.data)