
from django.urls import path
from main import views

from petproj import settings

app_name = 'main'
urlpatterns = [

    path('', views.MainPageView.as_view(), name='home'),
]

