from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import BEDROOM_CHOICES,STATE_CHOICES,PRICE_CHOICES

def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    context = {
        'listings' : listings,
        'bedroom_choices' : BEDROOM_CHOICES,
        'state_choices' : STATE_CHOICES,
        'price_choices' : PRICE_CHOICES
    }
    return render(request,'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request,'pages/about.html',context)
