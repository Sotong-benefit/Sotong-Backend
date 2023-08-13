from django.contrib import admin
from .models import Community, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 1
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

# Register your models here.
@admin.register(Community)
class CommunityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'section' ,'description', 'created_at', 'title', 'user',)
    list_filter = ('created_at',)
    search_fields = ('id',)
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    inlines = [CommentInline]
    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()
