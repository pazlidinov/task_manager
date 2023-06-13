from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # profile
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    
    # login
    path('login/', views.login_page, name='login'),
    
    # logout
    path('logout/', views.logout_page, name='logout'),
    
    # registration
    path('registration/', views.registration_page, name='registration'),
    
    # profile_edit
    path('profile_edit/<pk>', views.ProfileUpdateView.as_view(), name='profile_edit'),
]

