# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blogs/index.html")

def new(request):
    return render(request, "blogs/new.html")

def number(request, number):
    context = {
        'number': number
    }
    return render(request, "blogs/shownumber.html", context)