from django.db import models

class UploadedBenefit(models.Model):
    file = models.ImageField(upload_to='uploaded_images/')
    tag = models.TextField(verbose_name='태그')

class Counter(models.Model):
    count = models.IntegerField(default=0)


