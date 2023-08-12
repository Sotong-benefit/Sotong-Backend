from django.contrib import admin

from .models import UploadImage

@admin.register(UploadImage)
class TongTongModelAdmin(admin.ModelAdmin):
    list_display = ('image','tag')