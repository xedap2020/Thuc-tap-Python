from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', GradeList.as_view(), name='grade-list'),
    path('create', AddGrade.as_view(), name='add-grade'),
    path('<int:pk>', GradeDetail.as_view(), name='grade-detail'),
    path('edit/<int:pk>', EditGrade.as_view(), name='edit-grade'),
    path('delete/<int:pk>', DeleteGrade.as_view(), name='delete-grade'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
