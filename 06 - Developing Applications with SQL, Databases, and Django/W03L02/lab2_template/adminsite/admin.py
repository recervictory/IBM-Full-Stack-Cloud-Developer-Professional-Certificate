from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.
admin.site.register(Course)
admin.site.register(Instructor)