
from rest_framework.views import APIView

from student.models import Student
from .serializers import StudentSerializer

from classes.models import Classes
from .serializers import ClassesSerializer

# from .views import StudentDetailView

from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer


from course.models import Course
from .serializers import CourseSerializer

from teacher.models import Teacher
from .serializers import TeacherSerializer

from rest_framework.response import Response

from rest_framework.views import status



class StudentListView(APIView):
    def get (self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=
                            status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=
                            status.HTTP_400_BAD_REQUEST) 
class StudentDetailView(APIView):
    def get(self, request, id):
        student= Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data) 

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATEDH) 
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        student = Student.objects.get(id= id) 
        student.delete()
        return Response (status=status.HTTP_202_ACCEPTED)   
              

class ClassPeriodListView(APIView):
    def get (self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod= ClassPeriod.objects.get(id=id)
        Serializer = ClassPeriodSerializer(classperiod)
        return Response(Serializer.data) 

    def put(self, request, id):
        classPeriod = ClassPeriod.objects.get()
        serializer = ClassPeriodSerializer(classPeriod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        classPeriod = ClassPeriod.objects.get(id=id) 
        ClassPeriod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)   
              
    
class TeacherListView(APIView):
    def get (self, request):
        teacher = Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request):
        teacher= Teacher.objects.get()
        Serializer = TeacherSerializer(teacher, many=True)
        return Response(Serializer.data) 

    def put(self, request, id):
        serializer = TeacherSerializer.objects.get()
        serializer = TeacherSerializer(Teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        ClassPeriod = ClassPeriod.objects.get() 
        ClassPeriod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)   
 
class CourseListView (APIView):
    def get (self, request):
        course = Course.objects.all()
        serializer=CourseSerializer(course, many= True)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
class  ClassesListView (APIView):
    def get (self,request):
        classes = Classes.objects.all()
        serializer =  ClassesSerializer(classes,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
class ClassesDetailView(APIView):
    def get(self,request, id):
        classes= Classes.objects.get(id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    def put(self,request,id):
        classes=Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classes=Classes.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CourseDetailView(APIView):
    def get (self, request):
        course= Course.objects.all()
        serializer=CourseSerializer(course, many= True)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = CourseSerializer.objects.get()
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        course = Course.objects.get() 
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)   

              
