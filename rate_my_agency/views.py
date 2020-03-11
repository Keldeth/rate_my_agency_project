from django.shortcuts import render
from rate_my_agency.models import City
from rate_my_agency.models import Agency

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # query db for list of all cities to display
    city_list = City.objects.order_by('name')[:]

    context_dict = {}
    context_dict['boldmessage'] = 'This is the home page of Rate My Agency.'
    context_dict['cities'] = city_list
    
    return render(request, 'rate_my_agency/index.html', context=context_dict)

def about(request):
    return render(request, 'rate_my_agency/about.html')

def show_city(request, city_name_slug):
    context_dict = {}

    try:
        # get city with this associated slug, or raise exception
        city = City.objects.get(slug=city_name_slug)

        # retrieve list of all agencies in this city
        agencies = Agency.objects.filter(city=city)

        # add results to template context
        context_dict['agencies'] = agencies
        context_dict['city'] = city

    except City.DoesNotExist:
        context_dict['city'] = None
        context_dict['agencies'] = None

    return render(request, 'rate_my_agency/city.html', context=context_dict)
        
