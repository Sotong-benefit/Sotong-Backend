from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

# Create your models here.

class Community(models.Model):
    image = models.ImageField(verbose_name='이미지',null=True, blank=True)
    description = models.TextField(verbose_name='내용',null=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name='제목')

    user= models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=False)
    tag = models.ManyToManyField('tag.Tag', verbose_name = "태그")

    class Meta:
        db_table = 'community'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'community')

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    community = models.ForeignKey(to='Community', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)