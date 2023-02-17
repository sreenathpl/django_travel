from . import views
from django.urls import path

urlpatterns = [
    path('user_reg',views.user_reg,name='user_reg'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name= 'user_logout')
]