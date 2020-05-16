from django.urls import path
from home import views

urlpatterns = [   
    path('', views.index, name='Home'), 
    path('signup', views.handleSignup, name='Signup'),
    path('login', views.handleLogin, name='Login'),
    path('resetSend', views.handleResetSend, name='ResetSend'),
    path('resetReceive', views.handleResetReceive, name='ResetReceive'),
    path('signup_by_referal', views.signup_by_referal, name='Signup_by_referal'),
]
