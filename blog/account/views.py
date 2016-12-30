from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from account.forms import UserForm, UserProfileForm

def register(request):
    '''
    Register a new user
    '''
    template = 'account/register.html'
    if request.method=='GET':
        return render(request, template, {'userForm':UserForm(),'userProfileForm':UserProfileForm()})
    # POST
    userForm = UserForm(request.POST)# Create your views here.
    userProfileForm = UserProfileForm(request.POST)
    if not (userForm.is_valid() and userProfileForm.is_valid()):
        return render(request, template, {'userForm':userForm,'userProfileForm':userProfileForm})
    user = userForm.save()
    user.set_password(user.password)
    user.save()
    userProfile = userProfileForm.save(commit=False)
    userProfile.user = user
    userProfile.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')

def login(request):
    '''
    Login an existing user
    '''
    template = 'account/login.html'
    if request.method=='GET':
        return render(request, template, {'nextURL':request.GET.get('next')})
    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:
    # authentication fail
        messages.error(request, '登入失敗')
        return render(request, template)
    if not user.is_active:
        messages.error(request, '帳號已停用')
        return render(request, template)
    # login success
    auth_login(request, user)
    nextURL = request.POST.get('nextURL')
    if nextURL:
        return redirect(nextURL)
    messages.success(request, '登入成功')
    return redirect('main:main')

@login_required
def logout(request):
    '''
    Logout the user
    '''
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('main:main')