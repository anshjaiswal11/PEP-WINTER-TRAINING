
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booksViewSet.as_view({'get': 'list'}), name='books-list'),
    path('api/students', views.StudentViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='students-list'),
    path('students', views.StudentViewSet.as_view({'get': 'list', 'post': 'create' }), name='students-list-alt'),
]