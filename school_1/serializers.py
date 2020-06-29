from rest_framework import serializers
from .models import School, Class, Teacher, Student, Subject


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'SchoolName', 'created_at', 'updated_at']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'TeacherName', 'ClassName']
        depth = 2


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'FirstName', 'ClassName']
        depth = 1


class SearchsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'TeacherName']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'Subject', 'TeacherName']
        depth = 1


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'FirstName', 'LastName', 'ClassName']
        depth = 1


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'ClassName']
