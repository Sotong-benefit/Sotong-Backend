from django.shortcuts import render

from django.shortcuts import render, redirect

from findbenefit.models import Benefit, Like

def findbenefit(request):

    benefits = Benefit.objects.all()
    context = {
        'benefits': benefits
    }
    return render(request, 'findbenefit/benefit-album-page.html', context )

def bulletin(request):
    return render(request, 'findbenefit/find-benefit-bulletin.html')

def album(request):
    return render(request, 'findbenefit/benefit-album-page.html')

def benefitlist(request):
    return render(request, "findbenefit/benefit-list-page.html")

def post_section_view(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id') #좋아요를 누른 게시물id (blog_id)가지고 오기'
        

        print("post_id : " + post_id)

        if post_id != '':

            like_post = Benefit.objects.get(id=post_id) 
            # like_post = get_object_or_404(Community, id=post_id)

            if Like.objects.filter(user=request.user, benefit=like_post).exists():
                # 이미 좋아요를 눌렀을 경우 처리
                favorite = Like.objects.get(user=request.user, benefit=like_post)
                favorite.delete()
                print("성공")

            else:
                # 중개 모델을 생성하고 저장
                like = Like(user=request.user, benefit=like_post)
                like.save()

def newbenefit(request):
    benefits = Benefit.objects.all()
    context = {'benefits':benefits}
    #context에 모든 정보 저장
    return render(request, 'findbenefit/benefit-album-page.html', context)
