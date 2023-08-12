from django.contrib import admin

from .models import UploadedBenefit

@admin.register(UploadedBenefit)
class TongTongModelAdmin(admin.ModelAdmin):
    list_display = ('file','tag')
    # list_display = ('todolist',)