from django.contrib import admin
from .models import Calculator

# Register your models here.
@admin.register(Calculator)
class CommunityModelAdmin(admin.ModelAdmin):
    # list_display = ('marry', 'welfare', 'income_myself', 'imcome_fam', 'house', 'land', 'rental_deposit', 'property', 'car', 'finance', 'dept', 'user',)
    list_display = ('id', 'income', 'section', 'user',)
    search_fields = ('id',)
