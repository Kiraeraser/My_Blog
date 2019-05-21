from django.contrib import admin

# Register your models here.

#can also be used to save into th database using GUI
from .models import Blogpost
    
admin.site.register(Blogpost)

#run the server