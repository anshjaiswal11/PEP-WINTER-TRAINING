from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import books, Student
from .serializers import booksSerializer
from .serializers import StudentSerializer

class booksViewSet(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = booksSerializer



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

