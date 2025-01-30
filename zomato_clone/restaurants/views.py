from django.shortcuts import render, get_object_or_404
from .models import Restaurant, MenuItem, Review
from django.db.models import Q

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurants/restaurant_detail.html', {
        'restaurant': restaurant,
        'menu_items': menu_items,
        'reviews': reviews
    })

def search_restaurants(request):
    query = request.GET.get('q')
    restaurants = Restaurant.objects.filter(Q(name__icontains=query) | Q(cuisine__icontains=query))
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def filter_restaurants(request):
    cuisine = request.GET.get('cuisine')
    restaurants = Restaurant.objects.filter(cuisine=cuisine)
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})