# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
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

def create(request):
    # talk to model Manager
    result = User.objects.validate(request.POST)
    # result is either hanging onto (False, ['', '']) or (True, {first_name:"Todd", last_name:"ENders"})
    if result[0]:
        return redirect('/')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/users/new')
