from django.contrib import admin
from .models import Community

# Register your models here.
@admin.register(Community)
class CommunityModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'created_at', 'title', 'user',)
    list_filter = ('created_at',)
    search_fields = ('id',)
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'

    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()
