from django.shortcuts import render
from .models import Background_Image,Course_Feature,Registration,Contact,Excercise_home
from django.views.generic import View
from django.contrib import messages



# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        background = Background_Image.objects.filter(featured=True)
        feature = Course_Feature.objects.order_by('feature_order')
        context = {
            'feature': feature,
            'background': background,
            
        }
        return render(request, 'index.html', context)

def Exercise_home(request):

    exercises = Excercise_home.objects.all()
    context = {
        'exercises': exercises,        
    }
    return render(request, 'exercise_home.html', context=context)


def registration(request):    
    if request.method == "POST":
        name = request.POST.get("name")
        
        father_name = request.POST.get("father_name")
        phone = request.POST.get("phone")
        grade = request.POST.get("grade")
        course = request.POST.get("course")
        email = request.POST.get("email")
        city = request.POST.get("city")

        new_registration = Registration()
        new_registration.name = name
        new_registration.email = email
        new_registration.father_name = father_name
        new_registration.phone = phone
        new_registration.grade = grade
        new_registration.course = course
        new_registration.city = city

        new_registration.save()
        messages.success(request, 'Thanks for showing interest! We will contact you soon')    
    return render(request,'register.html')

def contact(request):    
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        message_type = request.POST.get("message_type")
        
        email = request.POST.get("email")
        message = request.POST.get("message")

        new_message = Contact()
        new_message.first_name = first_name
        new_message.email = email
        new_message.last_name = last_name
        new_message.message_type = message_type
        new_message.message = message
        

        new_message.save()
        messages.success(request, 'Thanks for showing interest! We will contact you soon')    
    return render(request,'contact.html')
