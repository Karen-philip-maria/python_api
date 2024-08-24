
from rest_framework.views import APIView

from student.models import Student
from .serializers import StudentSerializer

from classes.models import Classes
from .serializers import ClassesSerializer

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
        first_name = request.query_params.get("first_name")
        contry = request.query_params.get("country")
        if first_name:
            student = Student.objects.filter(first_name= first_name)
            if country:
                student= Student.objects.filter(country=country)
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

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")

        if action =="enroll":
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)
            return Response(status.HTTP_202_ACCEPTED) 
        
        if action =="unenroll":
            course_id = request.data.get("course")
            self.unenroll_student(student, course_id)
            return Response(status.HTTP_202_ACCEPTED) 
    
        elif action == "add_to_class":
             class_id = request.data.get("classes")
             self.add_to_class(student, class_id)
             return Response(status=status.HTTP_202_ACCEPTED)   
      

    def enroll_student(self, student, course_id):
        course= Course.objects.get(id = course_id)
        student.courses.add(course)

    def unroll_student(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)

    def add_to_class(self, student, class_id):
        class_obj = Classes.objects.get(id= class_id)
        student.classes.add(class_id)    


    def get(self, request, id):
        student= Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data) 

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
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
        classperiod = ClassPeriod.objects.get()
        serializer = ClassPeriodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classPeriod = ClassPeriod.objects.get(id=id) 
        ClassPeriod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)   
              
    def post(self, request):
        serializer = ClassPeriodSerializer(data= request.data)
        if serializer.is_valid():
            class_period = serializer.save()

            teacher_id = request.data.get("teacher_id")
            Course_id  = request.dat.get("course_id")

            if teacher_id and course_id:
                teacher = Teacher.objects.get(id=teacher_id)
                course = Courses.objects.get(id=course_id)
                class_period.teacher = teacher
                class_period.course = course
                class_period.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TeacherListView(APIView):
    def get (self, request):
        teacher = Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many= True)
        teacher_code = request.query_params.get("teacher code")
        email = request.query_params.get("email")
        if teacher_code:
            teacher = teacher.filter(teacher_code == teacher_code)
        if email:
            email - email.filter(email == email)
        return Response(serializer.data)    
        
        # return Response(serializer.data)
    
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
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        teacher= Teacher.objects.get(id=id) 
        serializer= TeacherSerializer(teacher)
        teacher.delete()
        return Response (serializer.errors, status=status.HTTP_202_ACCEPTED)   
 
    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.course.add(course)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")

        if action == "assign_course":
            course_id = request.data.get("course")
            self.assign_course(teacher, course_id)
            return Response(status.HTTP_201_CREATED)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)    




class CourseListView (APIView):
    def get (self, request):
        course = Course.objects.all()
        serializer=CourseSerializer(course, many= True)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = CourseSerializer(course, data=request.data)
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

              
