from django.db import models

#photo
#name
#designation
#fb link
#twitter link
#created link

# Create your models here.
class Team(models.Model):
    
        first_name=models.CharField(max_length=255)
        last_name=models.CharField(max_length=255)
        designation=models.CharField(max_length=255)
        photo=models.ImageField(upload_to='photos/%Y/%m/%d/') #for this install pillow:using pip install pillow.pillow is a 3rd party python imaging library
        facebook_link=models.URLField(max_length=100)
        twitter_link=models.URLField(max_length=100)
        google_plus_link=models.URLField(max_length=100)
        created_date=models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.first_name