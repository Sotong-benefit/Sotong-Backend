from django.contrib import admin

from findbenefit.models import Benefit

# Register your models here.
@admin.register(Benefit)
class CommunityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'tag', 'user',)
    search_fields = ('id',)
    
    actions = ['make_published']