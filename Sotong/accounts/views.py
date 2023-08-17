from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomAuthForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model

from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib import messages
from django.core.exceptions import PermissionDenied
import ssl
from django.core.mail import get_connection

from .helpers import email_auth_num
from .forms import CustomSetPasswordForm

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from communities.models import Community, Favorite
from calculators.models import Calculator
from .forms import RecoveryPwForm

from config.settings import base

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
    
        
# 비밀 번호 찾기 페이지
@login_required
def recovery_pw_view(request):
    #template_name = 'Account/find.html'
    template_name = 'Account/recovery_pw.html'
    
    if request.method == 'GET':
        form = RecoveryPwForm()
        return render(request, template_name, {'form': form})


# 비밀번호찾기 창에서 필드 값들을 입력하고 Ajax요청을 하는 view
def ajax_find_pw_view(request):
    username = request.POST.get('username')
    user = User.objects.get(username=username)
    print('test')
    if user:
        # auth_num = email_auth_num()
        # user.last_name = auth_num 
        # user.save()
        

        # subject = '비밀번호 찾기 인증메일입니다.'
        # from_email = 'xogk1128@naver.com'
        # recipient_list = ['xogk1128@naver.com']
        # auth_num = email_auth_num()

        # #text_content = render_to_string('Account/recovery_email.txt', {'auth_num': auth_num })
        # html_content = render_to_string('Account/recovery_email.html', {'auth_num': 12 })

        # msg = EmailMultiAlternatives(subject, '', from_email, recipient_list)
        # msg.attach_alternative(html_content, "text/html")

        # # ...

        # msg.send()

        subject = 'Subject Here'
        message = 'Here is the message.'
        from_email = 'xogk1128@naver.com'
        recipient_list = ['xogk1128@naver.com']

        send_mail(subject, message, from_email, recipient_list)
        
    return redirect('index')
    #return HttpResponse(json.dumps({"result": user.username}, cls=DjangoJSONEncoder), content_type = "application/json")

def auth_confirm_view(request):
    username = request.POST.get('username')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = User.objects.get(username=username, last_name=input_auth_num)
    target_user.last_name = ""
    target_user.save()
    request.session['auth'] = target_user.username  
    
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")


def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(user_id=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)
        
        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('Account:login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'Account/password_reset.html', {'form':reset_password_form})