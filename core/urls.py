from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_page/', views.register_page, name='register_page'),
    path('update_user/', views.update_user, name='update_user'),
    path('<int:pk>/', views.chat, name='chat'),
]

