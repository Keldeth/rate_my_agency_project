from django.contrib import admin
from django.urls import path
from django.urls import include
from rate_my_agency import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('rate_my_agency/', include('rate_my_agency.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
