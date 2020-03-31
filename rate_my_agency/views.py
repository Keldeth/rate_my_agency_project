from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UserForm, CommentForm, TenantForm, AgencyForm
from .models import City, Agency, Tenant
from .filters import AgencyFilter

from django.views.generic import CreateView # Added Import

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # query db for list of all cities to display
    city_list = City.objects.order_by('name')[:]
    agencies = Agency.objects.all()
    myFilter = AgencyFilter(request.GET, queryset=agencies)
    agencies = myFilter.qs[:10]
    
    context_dict = {}
    context_dict = {'agencies':agencies, 'myFilter':myFilter,
                    'boldmessage':"This is the home page of Rate My Agency."}
    if city_list:
        context_dict['cities'] = city_list
    
    return render(request, 'rate_my_agency/index.html', context_dict)

def about(request):
    return render(request, 'rate_my_agency/about.html')

def show_city(request, city_name_slug):
    context_dict = {}

    try:
        # get city with this associated slug, or raise exception
        cities = City.objects.get(slug=city_name_slug)

        # retrieve list of all agencies in this city
        agencies = Agency.objects.filter(cities=cities)

        # add results to template context
        context_dict['agencies'] = agencies
        context_dict['cities'] = cities

    except City.DoesNotExist:
        context_dict['cities'] = None
        context_dict['agencies'] = None

    return render(request, 'rate_my_agency/city.html', context=context_dict)

def add_comment(request ,agency_profile_name):
    try:
        agency = AgencyProfile.objects.get(agency=agency_profile_name)
    except Agency.DoesNotExist:
        agency = None

    if agency is None:
        return redirect('/rate_my_agency/')
    
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            if agency:
                comment = form.save(commit=False)
                comment.agency = agency
                #comment.tenant = ???
                comment.save()
            form.save(commit=True)
            return redirect('/rate_my_agency/')
        else:
            print(form.errors)
    context_dict = {'form':form, 'agency':agency}
    return render(request, 'rate_my_agency/add_comment.html', context=context_dict)


def register(request):
    return render(request, 'rate_my_agency/register.html')

    
def register_agency(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        agency_form = AgencyForm(request.POST)
        
        if agency_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            agency = agency_form.save(commit=False)
            agency.user = user
            agency.save()
            agency_form.save_m2m()
            agency.save()
           
            registered = True
        else:
            print(user_form.errors, agency_form.errors)
    else:
        user_form = UserForm()
        agency_form = AgencyForm()
        

    return render(request, 'rate_my_agency/register_agency.html',
                  context = {'user_form': user_form, 'agency_form': agency_form, 'registered': registered})


def register_tenant(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        tenant_form = TenantForm(request.POST)
        
        if tenant_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            tenant = tenant_form.save(commit=False)
            tenant.user = user
            tenant.save()
            registered = True
        else:
            print(user_form.errors, tenant_form.errors)
    else:
        user_form = UserForm()
        tenant_form = TenantForm()
        

    return render(request, 'rate_my_agency/register_tenant.html',
                  context = {'user_form': user_form, 'tenant_form': tenant_form, 'registered': registered})





