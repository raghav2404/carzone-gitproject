from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

   path('',views.cars,name='cars'),
   path('<int:id>',views.car_detail,name='car_detail'),
    #route to individual car page on clicking on a featured/latest car from home page using its id from car db model--this is a dynamic path in django which changes url based on id value
   path('search',views.search,name='search'),
]