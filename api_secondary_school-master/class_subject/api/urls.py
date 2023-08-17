from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', ClassSubjectList.as_view(), name='class-subject-list'),
    path('create', AddClassSubject.as_view(), name='add-class-subject'),
    path('<int:pk>', ClassSubjectDetail.as_view(), name='class-subject-detail'),
    path('delete/<int:pk>', DeleteClassSubject.as_view(), name='delete-class-subject'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
