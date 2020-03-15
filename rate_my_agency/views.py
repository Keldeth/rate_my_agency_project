from django.shortcuts import render
from django.shortcuts import redirect
from rate_my_agency.forms import CommentForm, TenantForm, AgencyForm
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
    
def register_agency(CreateView):
    model = User
    form_class = AgencyForm
    template_name = 'agency.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agency'
        return super().get_context_data(**kwargs)

    def form_is_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('rate_my_agency:index')
    

def register_tenant(CreateView):
    model = User
    form_class = TenantForm
    template_name = 'tenant.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tenant'
        return super().get_context_data(**kwargs)

    def form_is_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('rate_my_agency:index')





    """
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rate_my_agency/register.html',
                  context = {'user_form': user_form,
                             'profie_form': profile_form,
                             'registered': registered})

    """
