from django.urls import path
from client import views

urlpatterns = [
    path('', views.index, name='Client'),
    path('profile', views.profile, name='Profile'),
    path('password', views.password, name='Password'),
    path('bank', views.bank, name='Bank'),
    path('transaction', views.transaction, name='Transaction'),
    path('membership/', views.membership, name='Membership'),
    path('client_list', views.client_list, name='Client_list'),
    path('add_client', views.add_client, name='Add_client'),
    path('my_referal_code', views.my_referal_code, name='My_referal_code'),
    path('contact', views.contact, name='Contact'),
    path('logout', views.handleLogout, name='HandleLogout'),
]
