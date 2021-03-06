from django.urls import path, include
from django.contrib import admin
from course import views

urlpatterns = [
    # class based view
    path('cbv/list/', views.CourseList.as_view(), name="cbv-list"),
    path('cbv/detail/<int:pk>', views.CourseDetail.as_view(), name="cbv-detail")
]