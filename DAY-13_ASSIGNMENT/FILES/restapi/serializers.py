from rest_framework import serializers
from .models import books

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'course']
