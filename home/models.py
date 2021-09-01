from django.db import models

# Create your models here.

class Fav_icon(models.Model):
    # png_image

    image = models.ImageField()

class Excercise_home(models.Model):
    exercise_name = models.CharField(max_length=100)
    exercise_link = models.CharField(max_length=500)
    leaderboard_link = models.CharField(max_length=500)
    updated_date = models.DateField()

    def __str__(self):
        return self.exercise_name

class Registration(models.Model):
    # png_image
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Contact(models.Model):
    # png_image
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message_type = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.message
        
class Background_Image(models.Model):
    # png_overlay
    
    title = models.CharField(max_length=100)
    image_jpg = models.ImageField()
    featured = models.BooleanField()
    overlay_png_image = models.ImageField()
    backrground_image_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

class Course_Feature(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    thumbnail_on_click = models.ImageField()
    featured = models.BooleanField()
    feature_order = models.IntegerField(unique=True, default = 1)

    def __str__(self):
        return self.title


