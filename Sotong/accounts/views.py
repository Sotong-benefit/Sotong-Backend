from django.shortcuts import render, redirect
# from .forms import UserCreateForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CustomAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

def signup_view(request):
    # Get 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form' : form }
        return render(request, 'Account/join.html', context)
    else:
        
        form = SignUpForm(request.POST)

        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('accounts:login')
        else:
            #리다이렉트
            return redirect('accounts:signup')

def login_view(request):
    
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'Account/login.html', { 'form' : CustomAuthForm() })
    else:
        # 데이터 유효성 검사
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            return redirect('accounts:login')
        user = authenticate(request, username=user, password=password)

        if user is not None:
            login(request, user)
                    # 응답
            return redirect('index')
            
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            return render(request, 'Account/login.html', {'form':CustomAuthForm()})
        
            # username = request.POST.get('username')
            # if username == '' or username == None:
            #     pass
            # user = User.objects.get(username=username)
            # if user == None:
            #     pass

        
def logout_view(request):
    # 데이터 유효성 검사
    if request.user.is_authenticated:
        # 비즈니스 로직 처리 - 로그아웃
        logout(request)
    # 응답
    return redirect('index')
