from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from tongtong.views import tongtong, upload

app_name = 'tongtong'

urlpatterns = [
    path('', tongtong, name='tongtong'),
    path('upload/', upload, name='upload'),
    # path('increase_count/', increase_count, name='increase_count'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로 추가