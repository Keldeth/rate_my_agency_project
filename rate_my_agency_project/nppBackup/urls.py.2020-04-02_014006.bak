from django.contrib import admin
from django.urls import path
from django.urls import include
from rate_my_agency import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rate_my_agency/', include('rate_my_agency.urls')),
    path('admin/', admin.site.urls),
]
