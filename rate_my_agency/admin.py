from django.contrib import admin
from rate_my_agency.models import City, Tenant, Agency, Rating, Comment, AgencyProfile

# Class added to customise the Admin Interface to fill in slug field as you give a city
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(City, CityAdmin)
admin.site.register(Tenant)
admin.site.register(Agency)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(AgencyProfile)
