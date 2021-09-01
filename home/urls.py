from django.urls import path
from .views import IndexView,registration,contact,Exercise_home

app_name = 'home'

urlpatterns = [    
    # path('',IndexView.as_view(), name='home1'),
    # path('exercise/',Exercise_home),
    path('',Exercise_home),
    path('register/',registration,name='register1'),
    
    path('contact/',contact,name='contact')
]

