from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', DepartmentList.as_view(), name='department-list'),
    path('create', AddDepartment.as_view(), name='add-department'),
    path('<int:pk>', DepartmentDetail.as_view(), name='department-detail'),
    path('edit/<int:pk>', EditDepartment.as_view(), name='edit-department'),
    path('delete/<int:pk>', DeleteDepartment.as_view(), name='delete-department'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
