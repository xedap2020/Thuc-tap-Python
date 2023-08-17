"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

is_api_enabled = settings.APP_MOD in (settings.APP_MOD_API, settings.APP_MOD_FULL)

urlpatterns = [
    path('admin/', admin.site.urls),
]

api_urls = [
    path('api/users/', include(('user.api.urls', 'api-user'), namespace='api-user')),
    path('api/grades/', include(('grade.api.urls', 'api-grade'), namespace='api-grade')),
    path('api/classes/', include(('classes.api.urls', 'api-class'), namespace='api-class')),
    path('api/subjects/', include(('subject.api.urls', 'api-subject'), namespace='api-subject')),
    path('api/departments/', include(('department.api.urls', 'api-department'), namespace='api-department')),
    path('api/school-years/', include(('school_year.api.urls', 'api-school-year'), namespace='api-school-year')),
    path('api/students/', include(('student.api.urls', 'api-student'), namespace='api-student')),
    path('api/points/', include(('point.api.urls', 'api-point'), namespace='api-point')),
    path('api/class-subjects/', include(('class_subject.api.urls', 'api-class-subject'), namespace='api-class-subject')),
    path('api/personal/', include(('personal.api.urls', 'api-personal'), namespace='api-personal')),
] if is_api_enabled else []

if is_api_enabled:
    urlpatterns += api_urls