from rest_framework import serializers
from .models import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = '__all__'

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specials
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'

class Fac_teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Fac_teacher
        fields = '__alll__'