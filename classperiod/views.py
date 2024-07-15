from django.shortcuts import render

from rest_framework.views import APIView
from classperiod.models import Course
from .serializers import classperiodSerializer
from rest_framework.response import Response

class classperiodListView(APIView):
    def get (self, request):
        classperiod = classperiod.objects.all()
        serializer = classperiodSerializer(Course, many= True)
        return Response(serializer.data)

# Create your views here.
