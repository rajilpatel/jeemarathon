from django.contrib import admin

# Register your models here.
from .models import Fav_icon, Background_Image, Course_Feature,Registration,Excercise_home

admin.site.register(Fav_icon)
admin.site.register(Background_Image)
admin.site.register(Course_Feature)
admin.site.register(Registration)
admin.site.register(Excercise_home)
