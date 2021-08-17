from django.shortcuts import render
from tester.models import Post
import random
# Create your views here.
def tester(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'tester.html')  

        else:
                return render(request,'tester.html')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
  
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('specialchar'):
        characters.extend(list('!@#$%^&*?<>'))    

    length = int(request.GET.get('length'))
    thepass= ''
    for x in range(length):
        thepass +=random.choice(characters)
    return render(request, 'password.html', {'password': thepass})

def about(request):
    return render(request, 'about.html')