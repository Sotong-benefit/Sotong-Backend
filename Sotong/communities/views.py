from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Community
from .forms import CommunityCreateForm


# Create your views here.

def index(request):

    return render(request, 'index.html')


def post_list_view(request):
    post_list = Community.objects.all().order_by('-created_at')
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
        return redirect('community:post-list')
    
def post_detail_view(request, id):
    
        try:
            post = Community.objects.get(id=id)
        except Community.DoesNotExist:
            return redirect('index')
        context = {
            'post':post,
        }
        return render(request, 'community/Bulletin-MyPost.html', context)

@login_required
def post_update_view(request, id):
    post = get_object_or_404(Community, id=id, user=request.user)
    # post = Post.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'post' : post
        }
        return render(request, 'community/Bulletin-edit.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        title = request.POST.get('title')
        tags = request.POST.get('tags')
        description = request.POST.get('description')
        
        if new_image:
            post.image.delete()
            post.image = new_image

        post.title = title
        post.tags = tags
        post.description = description
        post.save()

        
        return redirect('community:post-detail', post.id)

@login_required
def post_delete_view(request, id):
    if request.method == 'GET':
        post = get_object_or_404(Community, id=id)
        if post.user == request.user:
            post.delete()
    return redirect('community:post-list')
    