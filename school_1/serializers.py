from rest_framework import serializers
from .models import School, Class, Teacher, Student, Subject


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'SchoolName', 'created_at', 'updated_at']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'TeacherName', 'Class']
        # depth = 2


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'FirstName', 'ClassName']
        # depth = 1


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'Class', 'TeacherName']
        depth = 2


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'Subject', 'TeacherName']
        depth = 1



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'FirstName', 'LastName', ]
        depth = 1


class ClassSerializer(serializers.ModelSerializer):
    # Student = StudentsSerializer(many=True)

    class Meta:
        model = Class
        fields = ['id', 'ClassName', 'Student']
        depth = 1
