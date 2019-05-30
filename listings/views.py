from django.shortcuts import render, get_object_or_404

from .models import Listing
from .choices import BEDROOM_CHOICES,STATE_CHOICES,PRICE_CHOICES

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)

def search(request):
    query_set = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            query_set = query_set.filter(description__icontains=keywords) 

    
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            query_set = query_set.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            query_set = query_set.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            query_set = query_set.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            query_set = query_set.filter(price__lte=price) 

    context = {
        'bedroom_choices' : BEDROOM_CHOICES,
        'state_choices' : STATE_CHOICES,
        'price_choices' : PRICE_CHOICES,
        'listings' : query_set,
        'values' : request.GET    
    }
    return render(request, 'listings/search.html',context)

