from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True) #fetched data from db in form of objects
    all_cars=Car.objects.order_by('-created_date')
    data = {
      'teams' : teams,
      'featured_cars':featured_cars, #passed data to template in form of dictionary having  key as variable name and value as objects from db
      'all_cars':all_cars,
    }
    return render(request ,'pages/home.html',data)
# DB<--->VIEW<--->TEMPLATE
def about(request):
    teams=Team.objects.all()
    data={
        'teams' : teams,
    }
    return render(request,'pages/about.html',data)

def contact(request):
    return render(request,'pages/contact.html')

def services(request):
    return render(request,'pages/services.html')


    