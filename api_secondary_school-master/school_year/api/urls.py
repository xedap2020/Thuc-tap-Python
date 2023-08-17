from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', SchoolYearList.as_view(), name='school-year-list'),
    path('create', AddSchoolYear.as_view(), name='add-school-year'),
    path('<int:pk>', SchoolYearDetail.as_view(), name='school-year-detail'),
    path('edit/<int:pk>', EditSchoolYear.as_view(), name='edit-school-year'),
    path('delete/<int:pk>', DeleteSchoolYear.as_view(), name='delete-school-year'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
