from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

#In django a set of all objects of a model is called a Queryset which can be passed,sliced,modified using Model.objects.__()
def home(request):
    teams = Team.objects.all()
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True) #fetched data from db in form of objects
    all_cars=Car.objects.order_by('-created_date')
    #Fetch all distinct model,city,year, body style from Car Model/db
    #flat=True will fetch distinct values not tuples
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    data = {
      'teams' : teams,
      'featured_cars':featured_cars, #passed data to template in form of dictionary having  key as variable name and value as objects from db
      'all_cars':all_cars,
      'model_search':model_search,
      'city_search':city_search,
      'year_search':year_search,
      'body_style_search':body_style_search,
      
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message =request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding' +subject
        message_body ='Name:' + name + '. Email'+email+' . Phone: '+phone +'Message:'+message
        admin_info=User.objects.get(is_superuser=True)
        admin_email =admin_info.email
        send_mail(email_subject,message_body,'raghavrastogi1990@gmail.com',[admin_email],fail_silently=False,)
        messages.success(request,'Thanks for contacting. we will contact you shortly')
        return redirect('contact')
    return render(request,'pages/contact.html')

def services(request):
    return render(request,'pages/services.html')


    