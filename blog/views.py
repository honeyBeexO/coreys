from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'title':'AI & Business',        
        'date_posted':'August 27th, 2016',
        'catergory':'ChatGPT+',
        'content':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'short':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'author':'Fouzia'
    },
    {
        'title':'AI revolution',        
        'date_posted':'August 27th, 2016',
        'catergory':'ChatGPT+',
        'content':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'short':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'author':'Amin the 3rd'
    },
        {
        'title':'AI & Business',        
        'date_posted':'August 27th, 2016',
        'catergory':'ChatGPT+',
        'content':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'short':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'author':'Fouzia'
    },
    {
        'title':'AI revolution',        
        'date_posted':'August 27th, 2016',
        'catergory':'ChatGPT+',
        'content':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'short':'skhskjdhsjkhdhdskhdkjbdsdkjshd, kjhdkj iuyeds jsalij hd kdjhiuweh',
        'author':'Amin the 3rd'
    }
    
]
def home(request):
    #return HttpResponse('<h1>Blog Home Page View</h1>', data=[title])
    
    return render(request, 'blog/home.html',context={'title':'Home','posts':posts})

def about(request):
    #return HttpResponse('<h1>Blog About Page Function View</h1>')
    data ={
        'title':'About',
        'date':'23-08-2023 at Alger'
        }
    return render(request,'blog/about.html',context=data)