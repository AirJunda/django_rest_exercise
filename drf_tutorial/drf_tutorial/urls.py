"""drf_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
# for API doc
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from course import views

# for user api token
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(prefix='viewsets', viewset=views.CourseViewSet)

schema_view = get_schema_view(title='DRF API doc')

urlpatterns = [
    path('api-token-auth', obtain_auth_token),
    path('admin/', admin.site.urls), #DRF登录退出
    path('api-auth/', include('rest_framework.urls')),
    path('course/', include('course.urls')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='DRF API doc')),
    path('course/v2/', include(router.urls)),
]
