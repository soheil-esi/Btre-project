# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'pages/index.html')
def about (request) :
    return render(request , 'pages/about.html')