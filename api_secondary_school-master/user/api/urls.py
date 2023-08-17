from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('create', AddUser.as_view(), name='add-user'),
    path('<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('edit/<int:pk>', EditUser.as_view(), name='edit-user'),
    path('delete/<int:pk>', DeleteUser.as_view(), name='delete-user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
