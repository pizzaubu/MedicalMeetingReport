from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('home/', views.home, name='home'),  # URL สำหรับหน้าหลักหลังจาก login/register
]
