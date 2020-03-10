from django.contrib import admin
from rate_my_agency.models import City, Tenant, Agency, AgencyProfile, Rating, Comment

# Register your models here.
admin.site.register(City)
admin.site.register(Tenant)
admin.site.register(Agency)
admin.site.register(AgencyProfile)
admin.site.register(Rating)
admin.site.register(Comment)