from django.shortcuts import render
from .models import Lesson,LessonImage,Video
# Create your views here.
def index(request):
    return render(request,'learning/index.html')
def level_list(request):
    return render(request,'learning/level_list.html')
def level(request,level):
    level_text=['A1','A2','B1','B2']
    lesson_list=Lesson.objects.filter(level=level).order_by('number')
    context= {
        'lesson_list':lesson_list,
        'prev_section':None,
        'level':level_text[level],
    }
    return render(request,'learning/level.html',context)
def lesson(request,level,number):

    lesson = Lesson.objects.filter(level=level,number=number).first()
    lesson_imgs=LessonImage.objects.filter(lesson=lesson)
    context={
        'lesson_imgs':lesson_imgs
    }
    return render(request,'learning/lesson.html',context)
def alpha(request):
    return render(request,'learning/alpha.html')
def experience(request):
    return render(request,'learning/experience.html')
def discover(request):
    return render(request,'learning/discover.html')
def entertain(request):
    entertain_video = Video.objects.filter(category='entertain_video')
    song_video = Video.objects.filter(category='song')
    for i in song_video:
        print(i.image.url)
    context={
        'video':entertain_video,
        'song':song_video,
    }
    return render(request,'learning/entertain.html',context)