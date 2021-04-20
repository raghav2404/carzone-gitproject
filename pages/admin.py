from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin): # team model in admin customization
      
     def thumbnail(self,object):
           return format_html('<img src="{}" style="border-radius:50%" width="40" />'.format(object.photo.url))
     thumbnail.short_description="photo"      
     list_display =('id','thumbnail', 'first_name','designation','created_date') #display data from model Team in table form
     list_display_links =('id','thumbnail','first_name') #make id and first_name clickable
     search_fields =('first_name','last_name','designation') #search on these basis
     list_filter = ('designation',)  #filter on these basis
admin.site.register(Team,TeamAdmin) 
