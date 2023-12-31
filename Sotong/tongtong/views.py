from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UploadImage, Counter
from .forms import UploadImageForm

def tongtong(request):
    return render(request, 'TongTong.html')

# def upload(request):
#     if request.method == 'POST':
#         post=UploadImage()
        
#         post.image = request.FILES.get('image')
#         post.tag = request.POST.get('tag')

#         post.save()
        
#     return render(request, 'TongTong.html')    

def upload_success(request):
    counter = Counter.objects.first()
    return render(request, 'TongTong.html', {'counter': counter})

count = 0  # 초기 카운터 값

def upload(request):
    if request.method == 'POST':
        post = UploadImage()
        
        post.image = request.FILES.get('image')
        post.tag = request.POST.get('tag')

        post.save()

        if Counter.objects.filter(user=request.user).exists():
            counter = Counter.objects.get(user=request.user)
            counter.counts += 3

            request.session['tongtong'] = counter.counts
        else:
            counter = Counter(counts=0, user=request.user)
            counter.counts += 3
            counter.save()
            request.session['tongtong'] = counter.counts
        

        counter.save()
        # global count
        #count += 3  # 3개씩 증가
    return render(request, 'TongTong.html')

