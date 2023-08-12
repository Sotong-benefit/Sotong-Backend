from django.urls import path

from .views import post_list_view, post_create_form_view, test

app_name = 'community'

urlpatterns = [
    path('', post_list_view, name='post-list'),
    path('new/', post_create_form_view, name='post-create'),
    path('test/', test, name='test'),
]