from rest_framework import serializers
from course.models import classperiod

class classperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model=  classperiod
        fields="_all_"