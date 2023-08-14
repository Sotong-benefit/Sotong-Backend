from django.contrib import admin

from .models import UploadImage, Counter

@admin.register(UploadImage)
class TongTongModelAdmin(admin.ModelAdmin):
    list_display = ('image','tag')

@admin.register(Counter)
class CounterModelAdmin(admin.ModelAdmin):
    list_display = ('id','counts', 'user')