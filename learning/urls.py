from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name='learning'
urlpatterns = [
    path('',views.index ,name='index'),
    path('level/',views.level_list,name='level_list'),
    path('level/<int:level>/',views.level,name='level'),
    path('level/<int:level>/lesson/<int:number>/',views.lesson,name='lesson'),
    path('alpha/',views.alpha,name='alpha'),
    path('experience/',views.experience,name='experience'),
    path('discover/',views.discover,name='discover'),
    path('entertain/',views.entertain,name='entertain'),
]