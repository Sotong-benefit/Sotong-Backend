from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    tag = models.TextField(verbose_name='태그')

class Counter(models.Model):
    count = models.IntegerField(default=0)


