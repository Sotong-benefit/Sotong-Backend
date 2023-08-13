from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Calculator(models.Model):
    marry = models.IntegerField(verbose_name='여행경비', blank=False, null=False)
    welfare = models.IntegerField(verbose_name='복지 자격 여부', blank=False, null=False)
    income_myself = models.IntegerField(verbose_name='본인 소득', blank=False, null=False)
    imcome_fam = models.IntegerField(verbose_name='가구원 소득', blank=False, null=False)
    house = models.IntegerField(verbose_name='주택,건축물', blank=False, null=False)
    land = models.IntegerField(verbose_name='토지', blank=False, null=False)
    rental_deposit = models.IntegerField(verbose_name='임차 보증금', blank=False, null=False)
    property = models.IntegerField(verbose_name='기타 재산', blank=False, null=False)
    car = models.IntegerField(verbose_name='차량 가격', blank=False, null=False)
    finance = models.IntegerField(verbose_name='금융 재산', blank=False, null=False)
    dept = models.IntegerField(verbose_name='부채', blank=False, null=False)

    income = models.IntegerField(verbose_name='소득 인정액')
    section = models.CharField(verbose_name='구간', max_length=10, null=True, blank=True)

    user= models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=True)