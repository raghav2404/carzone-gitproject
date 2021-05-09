from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def cars(request):
     cars= Car.objects.order_by('-created_date')
     paginator=Paginator(cars,2) #no of data i.e cars we want to show in 1 page here its 3
     #This is pagination provided by paginator class of Django. Suppose there are 6 car objects they are split into 2 pages with 3 each
     page=request.GET.get('page')
     paged_cars=paginator.get_page(page)

     model_search=Car.objects.values_list('model', flat=True).distinct()
     city_search=Car.objects.values_list('city',flat=True).distinct()
     year_search=Car.objects.values_list('year',flat=True).distinct()
     body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
     data={
         'cars':paged_cars,
         'model_search':model_search,
         'city_search':city_search,
         'year_search':year_search,
         'body_style_search':body_style_search,
     }
     return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    data={
        'single_car':single_car,

    }
    return render(request, 'cars/car_detail.html',data)


def search(request):
    cars=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:#keyword is not blank
            cars=cars.filter(description__icontains=keyword)
            #we are searching for the searched keyword in cars model/db object-- description field
    elif 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars=cars.filter(model__iexact=model)
    elif 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)
    elif 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)
    
    elif 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars=cars.filter(body_style__iexact=body_style)

    elif 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte = min_price, price__lte =max_price)
        #show cars with price >= min price and <=max price
    data={
        'cars':cars,#This contains all those car object whose desc contain a keyword 'keyword' and model name from search sidebar on homepage
        #for sidebar search
         'model_search':model_search,
         'city_search':city_search,
         'year_search':year_search,
         'body_style_search':body_style_search,
         'transmission_search':transmission_search,
         }
    return render(request,'cars/search.html',data)