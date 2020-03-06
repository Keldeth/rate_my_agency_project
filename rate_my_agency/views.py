from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'This is the home page of Rate My Agency.'}
    return render(request, 'rate_my_agency/index.html', context=context_dict)


def about(request):
    return render(request, 'rate_my_agency/about.html')

