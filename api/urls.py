from  django.urls import path
from .views import StudentListView

from  django.urls import path
from .views import TeacherListView

from  django.urls import path
from .views import ClassListView

from  django.urls import path
from .views import CourseListView

from  django.urls import path
from .views import ClassPeriodListView



urlpatterns=[
    path("students/",StudentListView.as_view(), name="student_list_view")
]

urlpatterns=[
    path("teacher/",TeacherListView.as_view(), name="teacher_list_view")
]

urlpatterns=[
    path("class/",ClassListView.as_view(), name="class_list_view")
]

urlpatterns=[
    path("course/",CourseListView.as_view(), name="course_list_view")
]

urlpatterns=[
    path("classperiod/",ClassPeriodListView.as_view(), name="classperiod_list_view")
]