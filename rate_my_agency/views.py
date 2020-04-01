from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from .forms import UserForm, CommentForm, TenantForm, AgencyForm
from .models import City, Agency, Tenant, Comment, Rating
from .filters import AgencyFilter

# Imported for use in the index page
import operator

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
    comments = Comment.objects.all()
    all_agencies = Agency.objects.all()
    
    context_dict = {}
    context_dict = {'all_agencies':all_agencies, 'agencies':agencies, 'myFilter':myFilter,
                    'boldmessage':"This is the home page of Rate My Agency."}
    if city_list:
        context_dict['cities'] = city_list

    # Code to find agencies with higest ratings
    agency_ratings = {}
    for agency in all_agencies:
        agency_ratings[agency] = findRating(agency)
    ordered_ratings = sorted(agency_ratings.items(), key=operator.itemgetter(1), reverse=True)
    top_agencies = [ordered_ratings[0][0], ordered_ratings[1][0], ordered_ratings[2][0]]
    context_dict['top_agencies'] = top_agencies

    # Code to find agencies with most comments
    agency_comments = {}
    # loops through all comments and adds entries to a dictionary of form key=agency, value=number of comments
    for comment in comments:
        if comment.agency in agency_comments:
            agency_comments[comment.agency] += 1
        else:
            agency_comments[comment.agency] = 1

    # orders this list of agencies by their number of comments descendingly, and puts it in a list of tuples
    ordered_agencies = sorted(agency_comments.items(), key=operator.itemgetter(1), reverse=True)
    # takes the three top cities from this list
    busy_agencies = [ordered_agencies[0][0], ordered_agencies[1][0], ordered_agencies[2][0]]
    context_dict['busy_agencies'] = busy_agencies
    
    return render(request, 'rate_my_agency/index.html', context_dict)

# Helper method to find the overall percentage approval of an agency
def findRating(agency):
    good = 0
    bad = 0
    ratings = Rating.objects.filter(agency=agency)
    for rating in ratings:
        if rating.like == True:
            good += 1
        else:
            bad += 1

    if rating:
        total = good + bad
        return (good/total)*100
    else:
        return 0

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

def show_agency(request, agency_name_slug):
    context_dict = {}

    try:
        # get agency with associated slug
        agency = Agency.objects.get(slug=agency_name_slug)
        context_dict['agency'] = agency

    except Agency.DoesNotExist:
        context_dict['agency'] = None

    return render(request, 'rate_my_agency/agency.html', context=context_dict)

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




def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rate_my_agency:index'))
            else:
                return HttpResponse("Your Rate my Agency account is diabled.") 
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rate_my_agency/login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('rate_my_agency:index'))
   



