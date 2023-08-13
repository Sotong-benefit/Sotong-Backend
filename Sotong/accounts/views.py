from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomAuthForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model

from communities.models import Community, Favorite
from calculators.models import Calculator

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

@login_required
def myPage_view(request):
    my_post = Community.objects.all().order_by('-created_at').filter(user=request.user)

    favorite_communities = Favorite.objects.filter(user=request.user).values('community')

    # community_ids 리스트에 즐겨찾기한 community의 id들을 저장
    community_ids = [entry['community'] for entry in favorite_communities]

    # Community 모델에서 즐겨찾기한 community들을 가져옴
    my_favorite = Community.objects.filter(id__in=community_ids)

    section_res = Calculator.objects.all().filter(user=request.user)[0]

    context ={
        'my_post': my_post,
        'my_favorite' : my_favorite,
        'section_res' : section_res,
    }
    return render(request, 'Account/my-page.html', context)