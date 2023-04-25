from django.contrib import admin

from .models import Courses

class AdminCourses(admin.ModelAdmin):
    list_display=['course_name','fee','duration','start_date','trainer_name','trainer_exp','trainer_mode']
admin.site.register(Courses, AdminCourses)
