# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context=context_dict)
