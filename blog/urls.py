from django.urls import path
from . import views

#we specify the name because sometimes we want to do a reverse lookup on that route
#using the specific name makes it easier because we could be having multiple routes with the same
#name for example: Blog-> Home view, Store-> Home view. if we name them both home it wouldn't work 
urlpatterns = [
    path('',views.home, name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('profile/',views.about, name='blog-about'),
    path('post/',views.about, name='blog-about'),
    path('contact/',views.about, name='blog-about'),

]