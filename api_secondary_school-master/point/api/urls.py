from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', PointList.as_view(), name='point-list'),
    path('<int:pk>', PointDetail.as_view(), name='point-detail'),
    path('create', PointView.as_view(), name='add-point'),
    path('edit/<int:pk>', PointView.as_view(), name='edit-point'),
    path('delete/<int:pk>', PointView.as_view(), name='delete-point'),
    path('summary', PerformanceList.as_view(), name='performance-list'),
    path('summary/edit/<int:pk>', EditPerformance.as_view(), name='edit-performance'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
