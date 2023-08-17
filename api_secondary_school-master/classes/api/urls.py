from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', ClassesList.as_view(), name='classes-list'),
    path('create', AddClasses.as_view(), name='add-classes'),
    path('<int:pk>', ClassesDetail.as_view(), name='classes-detail'),
    path('edit/<int:pk>', EditClasses.as_view(), name='edit-classes'),
    path('delete/<int:pk>', DeleteClasses.as_view(), name='delete-classes'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
