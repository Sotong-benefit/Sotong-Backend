from django.contrib import admin
from django.urls import path

from tongtong.views import tongtong, upload_file

app_name = 'tongtong'

urlpatterns = [
    path('', tongtong, name='tongtong'),
    path('upload/', upload_file, name='upload_file'),
]
