from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Employee

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task
        
