from django.contrib import admin
from .models import CourseCategory, Course, Video


# Register your models here.
admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Video)