from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Community
from .forms import CommunityCreateForm


# Create your views here.

def index(request):

    return render(request, 'index.html')


def post_list_view(request):
    post_list = Community.objects.all()
    context ={
        'post_list': post_list
    }
    return render(request, 'community/community-main-page.html', context)

@login_required
def post_create_form_view(request):
    if request.method =='GET':
        form = CommunityCreateForm()

        context = {
            'form':form,
            }
        return render(request, 'community/Bulletin-writing.html',context)
    else:
        form = CommunityCreateForm(request.POST, request.FILES)
        
        
        if form.is_valid(): #유효성 검사 true
            tag = form.cleaned_data['tags']

            Community.objects.create(
                title=form.cleaned_data['title'],
                tags=tag,
                image=form.cleaned_data['image'],
                description=form.cleaned_data['description'],
                user=request.user
            )
        else: #유효성 검사 false
            print("유효성 검사 실패")
            errors = form.errors.as_data()  # 유효성 검사 실패 세부 정보
            for field, error_list in errors.items():
                field_name = form.fields[field].label  # 실패한 필드의 레이블 이름
                error_message = error_list[0].message  # 실패 메시지
                print(f"필드 '{field_name}': {error_message}")
            return redirect('community:post-create')
        return redirect('index')
    

def test(request):
    return render(request, 'community/Bulletin-MyPost.html')