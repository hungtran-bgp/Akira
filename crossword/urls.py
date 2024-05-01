from django.urls import path
from . import views
app_name='crossword'
urlpatterns = [
    path('<int:level>/',views.crossword_list,name='cross_list'),
    path('<int:level>/<int:id>/',views.crossword_detail,name='crossword'),
    path('result/<int:id>/',views.crossword_result,name='result'),
]