from django.urls import path

from rest_framework import status

from .views import StudentListView
from .views import CourseListView
from .views import ClassesListView
from .views import TeacherListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import ClassesDetailView
from .views import CourseDetailView
from .views import ClassPeriodDetailView


urlpatterns=[
    path("classperiods/",ClassPeriodListView.as_view(),name="classperiods_list_view"),

    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),

    path("student/",StudentListView.as_view(),name="student_list_view"),

    path("classes/",ClassesListView.as_view(),name="classes_list_view"),

    path("course/",CourseListView.as_view(),name="course_list_view"),

    
    path("student/<int:id>/",StudentDetailView.as_view(), name= "student_detail_view"),

    path("classperiod/<int:id>/", ClassPeriodDetailView.as_view(), name= "classPeriod_detail_view"),

    path ("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),

    path ("classes/<int:id>/", ClassesDetailView.as_view(), name="classes_detail_view"),

    path ("course/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
]
