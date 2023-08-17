from django.urls import path

from .views import signup_view, login_view, logout_view, myPage_view, myPage_plus_view, find_out_view, find_view, recovery_pw_view, ajax_find_pw_view, auth_confirm_view, auth_pw_reset_view


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('find/', find_view, name='find'),
    path('findOut/', find_out_view, name='findOut'),
    
    path('recovery/pw/', recovery_pw_view, name='recovery_pw'),
    path('recovery/pw/find/', ajax_find_pw_view, name='ajax_pw'),
    path('recovery/pw/auth/', auth_confirm_view, name='recovery_auth'),
    path('recovery/pw/reset/', auth_pw_reset_view, name='recovery_pw_reset'),


    path('myPage/', myPage_view, name='myPage'),
    path('myPage_plus', myPage_plus_view, name='myPage_plus')
]