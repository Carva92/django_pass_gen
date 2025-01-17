from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')

def password(request):

    

    characters = list('abcdefghijklmnopqrstuvxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!"#$%&/()?¡,.'))
    
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))   

    lenght = int(request.GET.get('lenght', 12)) #12 es el default

    thepassword = ''
    
    for _ in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

