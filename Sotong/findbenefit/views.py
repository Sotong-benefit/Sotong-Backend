from django.shortcuts import render, HttpResponse, JsonResponse
from .models import Post

def segment(request):
    if request.is_ajax():
        segment = request.GET.get('segment', None)
        if segment:
            posts = Post.objects.filter(segment=segment)
            data = [{'title': post.title, 'content': post.content} for post in posts]
            return JsonResponse({'posts': data})
    return HttpResponse(status=400)