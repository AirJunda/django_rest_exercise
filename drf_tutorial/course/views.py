from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework import viewsets


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
            s.save(teacher=self.request.user)

            return Response(data=s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self,request,pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            data = {'msg': "No such course"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        s = CourseSerializer(instance=obj)
        return Response(s.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            data = {'msg': "No such course"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        s = CourseSerializer(instance=obj,data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,pk):
        obj = self.get_object(pk=pk)
        if not obj:
            data = {'msg': "No such course"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" DRF viewset way to write same set of crud API views """
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # only need to overide this method as we definr our own rule for create logic
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)



