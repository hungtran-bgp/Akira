
from django.urls import path
from django.contrib.auth import views as authentication_views
from . import views
app_name='user'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.user_login,name='login'),
    #path('logout/',authentication_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.user_register,name='register'),
    path('profile/',views.user_profile,name='profile')
]