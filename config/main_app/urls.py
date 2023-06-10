from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
  path('', views.HomePageView.as_view(), name='home_page'),
]