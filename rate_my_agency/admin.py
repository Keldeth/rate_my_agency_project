from django.contrib import admin
from rate_my_agency.models import City, Tenant, Agency, Rating, Comment

# Class added to customise the Admin Interface to fill in slug field as you give a city
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Allows every agency to have a slug field filled in based on their username
class AgencyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('agencyName',)}

# Register your models here.
admin.site.register(City, CityAdmin)
admin.site.register(Tenant)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Rating)
admin.site.register(Comment)
