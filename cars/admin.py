from django.contrib import admin
from django.utils.html import format_html
from .models import Car
# Register your models here.

#car table in admin panel customization---display
class CarAdmin(admin.ModelAdmin):
      def thumbnail(self,object):
           return format_html('<img src="{}" style="border-radius:50%" width="40" />'.format(object.car_photo.url))
      thumbnail.short_description="Car Image" 
      list_display =('id','thumbnail','car_title','color','model','year','body_style','fuel_type', 'is_featured')
      list_display_links =('id','thumbnail','car_title')
      list_editable=('is_featured',)
      search_fields=('id','car_title','model') #search box created which searches on mentioned fields
      list_filter=('model','body_style','fuel_type','doors','state')

admin.site.register(Car,CarAdmin) 
                    #Car--Model havin Car db tables
                    #CarAdmin--Class to customize and display tables of Car db with fields in Admin panel

