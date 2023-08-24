from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Blog Home Page View</h1>', data=[title])
    
    return render(request, 'blog/home.html',context={'title':'Home'})

def about(request):
    #return HttpResponse('<h1>Blog About Page Function View</h1>')
    data ={
        'title':'About',
        'date':'23-08-2023 at Alger'
        }
    return render(request,'blog/about.html',context=data)