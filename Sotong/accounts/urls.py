from django.urls import path

from .views import signup_view, login_view, logout_view, myPage_view, myPage_plus_view, find_out_view, find_view, benefit_like_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('find/', find_view, name='find'),
    path('findOut/', find_out_view, name='findOut'),
    

    path('myPage/', myPage_view, name='myPage'),
    path('myPage_plus', myPage_plus_view, name='myPage_plus'),

    path('benefit', benefit_like_view , name='benefit-like')
]