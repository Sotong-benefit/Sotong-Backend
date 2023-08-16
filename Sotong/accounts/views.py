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
    email_msg = ''
    pwd_msg = ''
    # Get 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {
            'form' : form,
            'pwd_msg' : pwd_msg,
            'email_msg' : email_msg,
            }
        return render(request, 'Account/join.html', context)
    else:
        

        form = SignUpForm(request.POST)

        if form.is_valid():
            #리다이렉트
            email = request.POST.get('email')
            if User.objects.all().filter(email=email).exists():
                print("이메일 존재")
                msg = '이미 존재하는 이메일입니다.'
                context = {
                    'form' : form,
                    'pwd_msg' : pwd_msg,
                    'email_msg' : email_msg,
                }
                print(form.errors)
                return render(request, 'Account/join.html', context)
            else:
            #회원가입 처리
                instance = form.save()
                return redirect('accounts:login')
        else:
            # print(form.errors.as_data().get('password2'))
            

            if 'username' in form.errors:
                email_msg = form.errors.as_data().get('username')[0].messages[0]
                print(email_msg)

            if 'password2' in form.errors:
                pwd_msg = form.errors.as_data().get('password2')[0].messages[0]
                print(pwd_msg)

            
            context = {
                'form' : form,
                'pwd_msg' : pwd_msg,
                'email_msg' : email_msg,
            }
            return render(request, 'Account/join.html', context)

def login_view(request):
    
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'Account/login.html', { 'form' : CustomAuthForm() })
    else:
        # 데이터 유효성 검사
        form = CustomAuthForm(request, request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            # 응답
            return redirect('index')
            
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            context = {
                'form':CustomAuthForm(),
                'msg' : '아이디와 비밀번호가 일치하지 않습니다.'
            }
            
            return render(request, 'Account/login.html', context)
        

        
def logout_view(request):
    # 데이터 유효성 검사
    if request.user.is_authenticated:
        # 비즈니스 로직 처리 - 로그아웃
        logout(request)
    # 응답
    return redirect('index')

def find_view(request):
    return render(request, 'Account/find.html')

def find_out_view(request):
    return render(request, 'Account/find-out.html')

@login_required
def myPage_view(request):
    my_post = Community.objects.all().order_by('-created_at').filter(user=request.user)[:5]

    favorite_communities = Favorite.objects.filter(user=request.user).values('community')

    # community_ids 리스트에 즐겨찾기한 community의 id들을 저장
    community_ids = [entry['community'] for entry in favorite_communities]

    # Community 모델에서 즐겨찾기한 community들을 가져옴
    my_favorite = Community.objects.filter(id__in=community_ids)[:5]

    if Calculator.objects.all().filter(user=request.user).exists():
        section_res = Calculator.objects.all().filter(user=request.user)[0]
        income = section_res.income
        section = section_res.section
        income = format(income, ',')
    else:
        income = '-'
        section = '-'
    context ={
        'my_post': my_post,
        'my_favorite' : my_favorite,
        'income' : income,
        'section' : section,
    }
    return render(request, 'Account/my-page.html', context)

def myPage_plus_view(request):
    if request.GET.get('data') == '내가쓴글':
        my_post = Community.objects.all().order_by('-created_at').filter(user=request.user)[:8]
        context ={
            'my_post': my_post,
        }
        return render(request, 'Account/my_page_myself.html', context)
    
    elif request.GET.get('data') == '관심글':
        favorite_communities = Favorite.objects.filter(user=request.user).values('community')

        # community_ids 리스트에 즐겨찾기한 community의 id들을 저장
        community_ids = [entry['community'] for entry in favorite_communities]

        # Community 모델에서 즐겨찾기한 community들을 가져옴
        my_favorite = Community.objects.filter(id__in=community_ids)[:8]
        context ={
            'my_favorite' : my_favorite,
        }
        return render(request, 'Account/my_page_favorite.html', context)
    
