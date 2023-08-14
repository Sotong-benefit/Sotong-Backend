from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class UploadImage(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    tag = models.TextField(verbose_name='태그')

class Counter(models.Model):
    counts = models.IntegerField(default=0)
    user= models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=True)

