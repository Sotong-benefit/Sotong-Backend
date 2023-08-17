from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

# Create your models here.

class Community(models.Model):
    image = models.ImageField(verbose_name='이미지',null=True, blank=True)
    description = models.TextField(verbose_name='내용',null=False)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name='제목', null=False, blank=False)
    tags = models.CharField(verbose_name='태그', max_length=20)
    section = models.CharField(verbose_name='구간', max_length=10, null=True, blank=True)
    file = models.FileField(verbose_name='파일', null=True, blank=True)

    user= models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=False)
    

    class Meta:
        db_table = 'community'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'community')

class Comment(models.Model):
    content = models.CharField(max_length=100, verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    community = models.ForeignKey(to='Community', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)