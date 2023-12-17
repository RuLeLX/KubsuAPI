from rest_framework import serializers
from .models import *
import datetime

class StudentSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    time_create = serializers.SerializerMethodField()

    class Meta:
        model = Students
        fields = ['id_student', 'num_group', 'role', 'time_create']
    
    def get_role(self, obj):
        return 'Student'
    
    def get_time_create(self, obj):
        return datetime.datetime.now()

class TeacherSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    time_create = serializers.SerializerMethodField()

    class Meta:
        model = Teachers
        fields = ['id_teacher', 'email', 'role', 'time_create']

    def get_role(self, obj):
        return 'Teacher'
    
    def get_time_create(self, obj):
        return datetime.datetime.now()

class DecanSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    time_create = serializers.SerializerMethodField()

    class Meta:
        model = Decan
        fields = ['id_faculty', 'login', 'role', 'time_create']

    def get_role(self, obj):
        return 'Decan'
    
    def get_time_create(self, obj):
        return datetime.datetime.now()