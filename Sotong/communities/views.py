from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Community, Favorite, Comment
from .forms import CommunityCreateForm
from django.http import HttpResponse,JsonResponse
import json
from tongtong.models import Counter
from django.db.models import Q
from findbenefit.models import Benefit

# Create your views here.

def index(request):

    benefits = Benefit.objects.all()
    context = {
        'benefits': benefits
    }

    return render(request, 'index.html', context)


def post_list_view(request):
    post_list = Community.objects.all().order_by('-created_at')
    if request.user.is_authenticated:
        for post in post_list:
            post.is_liked = post.favorite_set.filter(user=request.user).exists()
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
            tags=form.cleaned_data['tags']
            section = 0
            if '1구간' in tags:
                section = 1
            elif '2구간' in tags:
                section = 2
            elif '3구간' in tags:
                section = 3
            elif '4구간' in tags:
                section = 4
            elif '5구간' in tags:
                section = 5
            elif '6구간' in tags:
                section = 6
            elif '7구간' in tags:
                section = 7
            elif '8구간' in tags:
                section = 8
            elif '9구간' in tags:
                section = 9
            elif '10구간' in tags:
                section = 10

            Community.objects.create(
                title=form.cleaned_data['title'],
                tags=tags,
                image=form.cleaned_data['image'],
                file=form.cleaned_data['file'],
                description=form.cleaned_data['description'],
                section = section,
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
            community = Community.objects.get(id=id)
            comments = Comment.objects.filter(community=community)
        except Community.DoesNotExist:
            return redirect('index')
        context = {
            'post':community,
            'comment_list' : comments,
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
        new_file = request.FILES.get('file')
        
        if new_image:
            post.image.delete()
            post.image = new_image

        if new_file:
            post.file.delete()
            post.file = new_file

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
    
@login_required
def comment_create_view(request):
    try:
        id = request.GET.get('post_id')
        content = request.GET.get('content')

        if request.user.is_authenticated:
            comment = Comment(
                writer = request.user,
                content = content,
                community = Community.objects.get(id=id)
            )
            comment.save()

        community = Community.objects.get(id=id)
        comments = Comment.objects.filter(community=community)

    except Community.DoesNotExist:
        return redirect('index')
    

    context = {
        'comment_list' : comments,
    }
    return render(request, 'community/comment_frame.html', context)

@login_required
def comment_update_view(request):
    id = request.FILES.get('comment_id')

    comment = get_object_or_404(Comment, id=id, writer=request.user)
    
    content = request.GET.get('text')
    post_id = request.GET.get('post_id')

    comment.content = content
    comment.save()

    community = Community.objects.get(id=post_id)
    comments = Comment.objects.filter(community=community)

    context = {
        'comment_list' : comments,
    }
    
    return redirect('community/comment_frame.html', context)

@login_required
def comment_delete_view(request):
    try:
        id = request.GET.get('comment_id')
        community_id = request.GET.get('post_id')

        comment = get_object_or_404(Comment, id=id)
        if comment.writer == request.user:
            comment.delete()

        community = Community.objects.get(id=community_id)
        comments = Comment.objects.filter(community=community)

    except Community.DoesNotExist:
        return redirect('index')
    

    context = {
        'comment_list' : comments,
        'post' : community
    }
    return render(request, 'community/comment_frame.html', context)

    
def post_section_view(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id') #좋아요를 누른 게시물id (blog_id)가지고 오기'
        section = request.GET.get('section')
        tags = request.GET.get('tags')
        writeType = request.GET.get('writeType')

        print("post_id : " + post_id)
        print("section : " + section)
        print("tags : " + tags)
        print("writeType : " + writeType)

        if post_id != '':

            like_post = Community.objects.get(id=post_id) 
            # like_post = get_object_or_404(Community, id=post_id)

            if Favorite.objects.filter(user=request.user, community=like_post).exists():
                # 이미 좋아요를 눌렀을 경우 처리
                favorite = Favorite.objects.get(user=request.user, community=like_post)
                favorite.delete()
                print("성공")

            else:
                # 중개 모델을 생성하고 저장
                like = Favorite(user=request.user, community=like_post)
                like.save()


        if section != '':
            post_list = Community.objects.all().order_by('-created_at').filter(section=section)
        else:
            post_list = Community.objects.all().order_by('-created_at')


        if writeType == '내가쓴글':
            post_list = post_list.filter(user=request.user)
        elif writeType == '내관심글':
            favorite_communities = Favorite.objects.filter(user=request.user).values('community')
            # community_ids 리스트에 즐겨찾기한 community의 id들을 저장
            community_ids = [entry['community'] for entry in favorite_communities]

            # Community 모델에서 즐겨찾기한 community들을 가져옴
            post_list = post_list.filter(id__in=community_ids)
        
        if tags != '':
            # 만약 해시태그를 적지 않은 경우
            noHashTag = tags.replace('#', '')
            noBlank = tags.replace(' ', '')
            post_list = post_list.filter(Q(tags__icontains=tags)| Q(tags__icontains=noHashTag) | Q(tags__icontains=noBlank))


        

        
            
            # if request.user.is_authenticated:
            #     for post in like_post:
            #         post.is_liked = post.favorite_set.filter(user=request.user).exists()

        if request.user.is_authenticated:
            for post in post_list:
                post.is_liked = post.favorite_set.filter(user=request.user).exists()

        context ={
            'post_list': post_list
        }

        return render(request, 'community/main_frame.html', context)