from django.urls import path
from . import views

app_name = 'mian_app'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    
    path('profile_project/', views.profile_project_add, name='profile_project'),
]
