from rest_framework import viewsets
from .models import ClassCodes, Professors, Students, Classes, EnrolledStudentClasses, Feedbacks
from .serializers import (ClassCodesSerializer, ProfessorsSerializer, StudentsSerializer, ClassesSerializer, EnrolledStudentClassesSerializer, FeedbacksSerializer)

class ClassCodesViewSet(viewsets.ModelViewSet):
    queryset = ClassCodes.objects.all()
    serializer_class = ClassCodesSerializer

class ProfessorsViewSet(viewsets.ModelViewSet):
    queryset = Professors.objects.all()
    serializer_class = ProfessorsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class EnrolledStudentClassesViewSet(viewsets.ModelViewSet):
    queryset = EnrolledStudentClasses.objects.all()
    serializer_class = EnrolledStudentClassesSerializer

class FeedbacksViewSet(viewsets.ModelViewSet):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer
