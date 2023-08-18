from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Benefit(models.Model):
    image = models.ImageField(verbose_name='이미지',null=False, blank=True)
    title = models.CharField(max_length=100, verbose_name='제목', null=False, blank=False)
    tag = models.CharField(max_length=100, verbose_name='태그', null=False, blank=False)

    user= models.ForeignKey(to=User, on_delete=models.CASCADE,null=False, blank=False)

    class Meta:
        db_table = 'benefit'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    

    # class Meta:
    #     unique_together = ('user', 'benefit')