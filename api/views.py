from django.shortcuts import render

from rest_framework.views import APIView

from student.models import Students
from .serializers import StudentSerializer

# from class.models import Class
# from .serializers import ClassSerializer

from classperiod.models import ClassPeriod
from .serializers import ClassperiodSerializer

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
