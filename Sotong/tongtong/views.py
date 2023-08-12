from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UploadImage, Counter
from .forms import UploadImageForm

def tongtong(request):
    return render(request, 'TongTong.html')

def upload(request):
    if request.method == 'POST':
        post=UploadImage()

        post.image = request.POSt['image']
        post.tag = request.POST['tag']

        post.save()
        
    #return render(request, 'TongTong.html')    

def upload_success(request):
    counter = Counter.objects.first()
    return render(request, 'TongTong.html', {'counter': counter})

# def upload_image(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
            
#             # 이미지 업로드 후 카운터 증가
#             counter = Counter.objects.first()
#             counter.count += 3
#             counter.save()
            
#             return redirect('upload_success')
#     else:
#         form = UploadImageForm()
    
#     counter = Counter.objects.first()
#     return render(request, 'upload_image.html', {'form': form, 'counter': counter})

# 혜택 이미지 업로드 AJAX
# def upload_file(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES.get('file')
#         tag = request.POST.get('tag', '')

#         if uploaded_file:
#             uploaded_benefit = UploadedBenefit.objects.create(image=uploaded_file, tag=tag)
            
#             # 통통이 개수를 증가시킴
#             counter = Counter.objects.first()
#             counter.count += 3  # 3개씩 증가시킴
#             counter.save()

#             return JsonResponse({'message': 'Success', 'uploaded_benefit_id': uploaded_benefit.id})
#         else:
#             return JsonResponse({'message': 'No file uploaded'}, status=400)
#     else:
#         return JsonResponse({'message': 'Invalid request'}, status=400)

# 혜택 이미지 업로드 form
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_benefit = form.save()

#             # 통통이 개수를 증가시킴
#             counter = Counter.objects.first()
#             counter.count += 3  # 3개씩 증가시킴
#             counter.save()

#             return JsonResponse({'message': 'Success', 'uploaded_benefit_id': uploaded_benefit.id})
#         else:
#             return JsonResponse({'message': 'Invalid form data'}, status=400)
#     else:
#         return JsonResponse({'message': 'Invalid request'}, status=400)
    

