from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserForm, CommentForm, TenantForm, AgencyForm, PictureForm
from .models import City, Agency, Tenant, Comment, Rating, Image
from .filters import AgencyFilter

# Imported for use in the index page
import operator

from django.views.generic import CreateView # Added Import

from django.shortcuts import render

from django.http import HttpResponse

# View for the index page
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
    #
    agency_ratings = {}
    # loops through all agencies and calculates their percentage approval based on likes/dislikes
    for agency in all_agencies:
        # uses helper method findRating()
        agency_ratings[agency] = findRating(agency)
    # sorts this dictionary of percentages into an ordered list of tuples (key=agency, value=approval)
    ordered_ratings = sorted(agency_ratings.items(), key=operator.itemgetter(1), reverse=True)

    top_agencies = []
    # adds the 3 highest rated agencies to top_agencies
    # takes into account case where there are less than 3 agencies in the database, and only tries to find them
    if len(ordered_ratings) < 3:
        for i in range(len(ordered_ratings)):
            top_agencies.append(ordered_ratings[i][0])
    else:
        top_agencies = [ordered_ratings[0][0], ordered_ratings[1][0], ordered_ratings[2][0]]
    context_dict['top_agencies'] = top_agencies


    # Code to find agencies with most comments
    #
    agency_comments = {}
    # loops through all comments and adds entries to a dictionary of form key=agency, value=number of comments
    for comment in comments:
        if comment.agency in agency_comments:
            agency_comments[comment.agency] += 1
        else:
            agency_comments[comment.agency] = 1

    # orders this list of agencies by their number of comments descendingly, and puts it in a list of tuples
    ordered_agencies = sorted(agency_comments.items(), key=operator.itemgetter(1), reverse=True)
    busy_agencies = []
    # takes the three top agencies from this list
    # if there are less than 3 agencies in the database it only displays these
    if len(ordered_ratings) < 3:
        for i in range(len(ordered_ratings)):
            busy_agencies.append(ordered_ratings[i][0])
    else:
        busy_agencies = [ordered_agencies[0][0], ordered_agencies[1][0], ordered_agencies[2][0]]
    context_dict['busy_agencies'] = busy_agencies
    
    return render(request, 'rate_my_agency/index.html', context_dict)

# Helper method to find the overall percentage approval of an agency
def findRating(agency):
    good = 0
    bad = 0
    ratings = Rating.objects.filter(agency=agency)
    # adds all of this agency's ratings to a good or bad counter
    for rating in ratings:
        if rating.like == True:
            good += 1
        else:
            bad += 1

    if ratings:
        # totals up the ratings, and finds the percentage that were "likes"
        total = good + bad
        return round((good/total)*100)
    else:
        return 0

#  View for the about page
def about(request):
    return render(request, 'rate_my_agency/about.html')

# View for city.html
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

# View for agency.html
def show_agency(request, agency_name_slug):
    context_dict = {}

    try:
        # get agency with associated slug
        agency = Agency.objects.get(slug=agency_name_slug)
        user = request.user
        tenant = Tenant.objects.get(user=user)

    except Tenant.DoesNotExist:
        context_dict['tenant'] = None
    except TypeError:
        context_dict['tenant'] = None
    else:
        context_dict['tenant'] = tenant
        context_dict['rating'] = Rating.objects.get(tenant=tenant, agency=agency) 
    finally:
        context_dict['agency'] = agency
        # again uses the findRating helper method
        context_dict['approval'] = findRating(agency)
        context_dict['comments'] = Comment.objects.filter(agency=agency)
        context_dict['images'] = Image.objects.filter(agency=agency)
        
        return render(request, 'rate_my_agency/agency.html', context=context_dict)

# View for add_comment.html
def add_comment(request ,agency_name_slug):
    commented = False
    try:
        agency = Agency.objects.get(slug=agency_name_slug)
        user = request.user
        tenant = Tenant.objects.get(user=user)
        
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
                comment.tenant = tenant 
                comment.save()

                commented = True
            form.save(commit=True)
            
        else:
            print(form.errors)
    context_dict = {'form':form, 'agency':agency, 'commented':commented }
    return render(request, 'rate_my_agency/add_comment.html', context=context_dict)

# View for creating a new raing of an agency by a tenant
def add_rating(request, agency_name_slug, like):
    agency = get_agency(agency_name_slug)

    user = request.user
    tenant = Tenant.objects.get(user=user)
    
    rating = {'like':like, 'tenant':tenant, 'agency':agency}
    r = Rating.objects.get_or_create(like = rating['like'], tenant = rating['tenant'], agency = rating['agency'])[0]
    r.save()
    context_dict = {'agency':agency}
    return context_dict

# View for a tenant clicking "like" on an agency page
def add_like(request, agency_name_slug):
    context_dict = add_rating(request, agency_name_slug, True)
    return render(request, 'rate_my_agency/add_like.html',context=context_dict)

# View for a tenant clicking "dislike" on an agency page
def add_dislike(request, agency_name_slug):
    context_dict = add_rating(request, agency_name_slug, False)
    return render(request, 'rate_my_agency/add_dislike.html',context=context_dict)

# View for a tenant deleting their rating of an agency
def delete_rating(request, agency_name_slug):
    agency = get_agency(agency_name_slug)
    
    user = request.user
    tenant= Tenant.objects.get(user=user)
    Rating.objects.get(tenant=tenant, agency=agency).delete()

    context_dict = {'agency':agency}
    return render(request, 'rate_my_agency/delete_rating.html',context=context_dict)

# View for the register page    
def register(request):
    return render(request, 'rate_my_agency/register.html')

# View for the register_agency page, for adding a new agency to the database
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

# View for the register_tenant page, for adding a new tenant to the database
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

# View for the login page
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

#View for the logout page
def user_logout(request):
    logout(request)
    return redirect(reverse('rate_my_agency:index'))

# View for the user profile page which displays a user's details
def view_profile(request):
    context_dict = {}
    try:
        tenant = Tenant.objects.get(user=request.user)
    except Tenant.DoesNotExist:
        context_dict['agency'] = Agency.objects.get(user=request.user)
        context_dict['tenant'] = None
    else:
        context_dict['tenant'] = tenant
    finally:
        context_dict['user'] = request.user
        return render(request, 'rate_my_agency/view_profile.html', context=context_dict)  

# View for the add_image page, for an agency adding a new image to the database
def add_image(request, agency_name_slug):
    added = False
    agency = get_agency(agency_name_slug)
    picture_form = PictureForm()

    try:
        if request.method == 'POST':
            picture_form = PictureForm(request.POST, request.FILES)
            if picture_form.is_valid():
                if agency and ('image' in request.FILES):
                    picture = picture_form.save(commit=False)
                    picture.image = request.FILES['image']
                    picture.agency = agency
                    picture.save()

                    added = True
                picture_form.save(commit=True)
            else:
                print(picture_form.errors)
    except (IntegrityError):
        return HttpResponseRedirect(reverse('rate_my_agency:add_image', args=(agency_name_slug,)))
    
    context_dict = {'picture_form':picture_form, 'agency':agency, 'added':added}
    return render(request, 'rate_my_agency/add_image.html', context=context_dict)

# View for the remove_images page, for removing all of an agency's images from the database
def remove_images(request, agency_name_slug):
    agency = get_agency(agency_name_slug)
    Image.objects.filter(agency=agency).delete()
    context_dict = {'agency':agency}
    return render(request, 'rate_my_agency/remove_images.html',context=context_dict)

# View for an agency page
def get_agency(agency_name_slug):
    try:
        agency = Agency.objects.get(slug=agency_name_slug)
        
    except Agency.DoesNotExist:
        agency = None

    if agency is None:
        return redirect('/rate_my_agency/')
    return agency

