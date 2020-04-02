from django.urls import path
from rate_my_agency import views

app_name = 'rate_my_agency'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('city/<slug:city_name_slug>/', views.show_city, name='show_city'),
    path('register/', views.register, name='register'),
    path('register/tenant/', views.register_tenant, name='register_tenant'),
    path('register/agency/', views.register_agency, name='register_agency'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('agency/<slug:agency_name_slug>/',
         views.show_agency, name='show_agency'),
    path('agency/<slug:agency_name_slug>/add_comment/', views.add_comment, name='add_comment'),
    path('agency/<slug:agency_name_slug>/like/', views.add_like, name='add_like'),
    path('agency/<slug:agency_name_slug>/dislike/', views.add_dislike, name='add_dislike')
    ]
