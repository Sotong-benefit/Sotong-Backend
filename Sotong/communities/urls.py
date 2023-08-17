from django.urls import path

from .views import post_list_view, post_create_form_view, post_detail_view, post_delete_view, post_update_view, post_section_view, comment_create_view, comment_delete_view

app_name = 'community'

urlpatterns = [
    path('', post_list_view, name='post-list'),
    path('new/', post_create_form_view, name='post-create'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('<int:id>/delete/', post_delete_view, name="post-delete"),
    path('<int:id>/edit/', post_update_view, name='post-update'),

    
    path('comment/new/', comment_create_view, name='comment-create'),
    path('comment/delete/', comment_delete_view, name='comment-delete'),

    # path('<int:id>/likes/', post_like_view, name='post-like'),

    # path('likes/', post_like_view, name='post-like'),
    path('sections/', post_section_view, name='post-section'),
]