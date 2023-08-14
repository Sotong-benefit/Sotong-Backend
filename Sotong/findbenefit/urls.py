from django.contrib import admin
from django.urls import path

from findbenefit.views import album, bulletin, findbenefit

app_name = 'findbenefit'

urlpatterns = [
    path('', findbenefit, name='findbenefit'),
    path('bulletin/', bulletin, name='bulletin'),
    path('album/', album, name='album'),
    
]
