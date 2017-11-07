# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def create_message(request):
    pass 

def create_comment(request):
    pass 

def logout(request):
    pass