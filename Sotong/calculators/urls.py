from django.urls import path

from .views import calc_view, result_view

app_name = 'calculator'

urlpatterns = [
    path('', calc_view, name='calc_view'),
    path('result/', result_view, name='result'),
]