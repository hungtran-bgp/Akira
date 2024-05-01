from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def index(request):
    return render(request,'user/index.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'user/login.html',{'err_msg':'Kiểm tra lại thông tin tài khoản'})
    else:
        return render(request,'user/login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

def user_register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'username_err': 'Tên tài khoảng này đã tồn tại'})
        if password1 != password2:
            return render(request, 'user/register.html', {'password_err': 'Xác nhận mật khẩu không đồng bộ'})
        user = User.objects.create_user(username=username, password=password1)
        return redirect('user:login')
    else :
        return render(request,'user/register.html')
@login_required
def user_profile(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.fullname = request.POST.get('fullname')
        profile.gender = request.POST.get('gender')
        profile.age = request.POST.get('age')
        profile.location = request.POST.get('location')
        profile.save()
        return redirect('user:profile')
    return render(request,'user/profile.html')