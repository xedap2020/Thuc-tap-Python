from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', SubjectList.as_view(), name='subject-list'),
    path('create', AddSubject.as_view(), name='add-subject'),
    path('<int:pk>', SubjectDetail.as_view(), name='subject-detail'),
    path('edit/<int:pk>', EditSubject.as_view(), name='edit-subject'),
    path('delete/<int:pk>', DeleteSubject.as_view(), name='delete-subject'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
