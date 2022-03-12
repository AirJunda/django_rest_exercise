from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.



"""Class Based View """

# 看了下flask，是用 if else去判断是get 还是post,然后分开处理

class CourseList(APIView):
    def get(self,request):
        queryset = Course.objects.all()
        s = CourseSerializer(instance=queryset,many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self,request):
        s = CourseSerializer(data=request.data)
        if s.is_valid():
            #s.save(teacher=self.request.user)
            s.save()
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
