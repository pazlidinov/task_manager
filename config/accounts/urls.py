
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.my_login, name='login'),
    path('', views.profile_page, name='profile'),
    
    path("logout/", auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),

]
