from django.contrib import admin
from django.urls import path

from findbenefit.views import findbenefit

app_name = 'findbenefit'

urlpatterns = [
    path('', findbenefit, name='findbenefit'),
]
