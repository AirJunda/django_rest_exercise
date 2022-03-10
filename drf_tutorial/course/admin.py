from django.contrib import admin

# Register your models here.
from .models import Course


#下面这个是JZ项目里的写法
#admin.site.register(Course)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduction','teacher', 'price')
    search_fields = list_display
    list_filter = list_display




