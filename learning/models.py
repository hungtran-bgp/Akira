from django.db import models

# Create your models here.
class Lesson(models.Model):
    level=models.PositiveIntegerField(default=0)
    number=models.IntegerField()
    vietnam_name=models.CharField(max_length=50)
    japan_name=models.CharField(max_length=50)
    note1=models.CharField(max_length=100,blank=True)
    note2=models.CharField(max_length=100,blank=True)
    section = models.PositiveIntegerField()
    section_title = models.CharField(max_length=100)
    def __str__(self):
        return f"level{self.level}:{self.vietnam_name}"
class LessonImage(models.Model):
    image=models.ImageField(upload_to='lesson_pictures')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Video(models.Model):
    image=models.ImageField(upload_to='video_pictures')
    url = models.CharField(max_length=600,default='None')
    category = models.CharField(max_length=30,default='None')