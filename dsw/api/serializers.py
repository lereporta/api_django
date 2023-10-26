from rest_framework import serializers
from .models import ClassCodes, Professors, Students, Classes, EnrolledStudentClasses, Feedbacks

class ClassCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCodes
        fields = '__all__'

class ProfessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professors
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class EnrolledStudentClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledStudentClasses
        fields = '__all__'

class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'
