from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template



def index(request):
    
    context = {
        'data': [
            {
                'students':'Natiea Cannon', 
                'tracks':'Backend(Python)', 
                'messages':'Hello mentor. Thank you for this excellect opportunity.',
            },
            ],
            }
  
    return render (request, 'newapp/index.html', context)
    