from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', StudentList.as_view(), name='student-list'),
    path('create', AddStudent.as_view(), name='add-student'),
    path('<int:pk>', StudentDetail.as_view(), name='student-detail'),
    path('edit/<int:pk>', EditStudent.as_view(), name='edit-student'),
    path('delete/<int:pk>', DeleteStudent.as_view(), name='delete-student'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
