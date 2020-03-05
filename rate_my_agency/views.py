from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='/rate_my_agency/about/'>About</a> Welcome to Rate My Agency")


def about(request):
    return HttpResponse("<a href='/rate_my_agency/'>Index</a> This is the about page")

