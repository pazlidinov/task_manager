from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('register/', views.register, name='register'),

]
