from django.shortcuts import render

from django.shortcuts import render, redirect

def findbenefit(request):
    return render(request, 'find-benefit-bulletin.html')



# def segment(request):
#     if request.is_ajax():
#         segment = request.GET.get('segment', None)
#         if segment:
#             posts = Post.objects.filter(segment=segment)
#             data = [{'title': post.title, 'content': post.content} for post in posts]
#             return JsonResponse({'posts': data})
#     return HttpResponse(status=400)