from django.urls import path
from rate_my_agency import views

app_name = 'rate_my_agency'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
