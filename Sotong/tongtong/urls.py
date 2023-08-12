from django.contrib import admin
from django.urls import path

from tongtong.views import tongtong

app_name = 'tongtong'

urlpatterns = [
    path('', tongtong, name='tongtong'),
]
