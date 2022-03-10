from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text='course info', verbose_name='Name of the course')
    introduction = models.TextField(help_text='course introduction', verbose_name='intro of the course')
    price = models.DecimalField(max_digits=6,decimal_places=2,help_text='course price')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                help_text='course instructor',  verbose_name='teacher of course')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created time')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='updated time')

    class Meta:
        verbose_name = 'course info'
        verbose_name_plural = verbose_name
        ordering = ('price',)

    def __str__(self):
        return self.name
