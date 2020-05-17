from django.urls import path
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [   
    path('', views.index, name='Home'), 
    path('signup', views.handleSignup, name='Signup'),
    path('login', views.handleLogin, name='Login'),
    path('signup_by_referal', views.signup_by_referal, name='Signup_by_referal'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="home/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_done.html"), 
        name="password_reset_complete"),
]
