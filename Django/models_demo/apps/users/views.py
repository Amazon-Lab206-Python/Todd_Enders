# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    all_users = User.objects.all() # SELECT * FROM users
    context = {
        'all_users': all_users
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')