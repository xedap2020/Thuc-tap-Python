from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('login', Login.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
