from django.shortcuts import render, redirect
from .models import UploadedImage, Counter
from .forms import UploadImageForm

def tongtong(request):
    return render(request, 'TongTong.html')

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            # 이미지 업로드 후 카운터 증가
            counter = Counter.objects.first()
            counter.count += 1
            counter.save()
            
            return redirect('upload_success')
    else:
        form = UploadImageForm()
    
    counter = Counter.objects.first()
    return render(request, 'upload_image.html', {'form': form, 'counter': counter})

def upload_success(request):
    counter = Counter.objects.first()
    return render(request, 'upload_success.html', {'counter': counter})