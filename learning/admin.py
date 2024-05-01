from django.contrib import admin
from .models import Lesson,LessonImage,Video
# Register your models here.
admin.site.register(Lesson)
admin.site.register(LessonImage)
admin.site.register(Video)