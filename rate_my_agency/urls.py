from django.urls import path
from rate_my_agency import views

app_name = 'rate_my_agency'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('city/<slug:city_name_slug>/',
         views.show_city, name='show_city'),
]
