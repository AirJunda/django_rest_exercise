from rest_framework import serializers
from .models import Course
from django.contrib.auth.models import User

from django import forms


class CourseSerializer(serializers.ModelSerializer):
    # 这里是想我们把外键关联的teach name也一并合并返回。
    teacher = serializers.ReadOnlyField(source='teacher.username') # foreign key field, read only
    class Meta:
        model = Course
        #exclude = ('id',)
        #fields = ('name', 'introduction', 'teacher', 'price')
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

