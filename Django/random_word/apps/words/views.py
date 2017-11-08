# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['word'] = get_random_string(length=14)
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 1
    return render(request, 'words/index.html')

def generate(request):
    request.session['counter'] += 1
    return redirect('/random_word')

def reset(request):
    request.session.clear()
    return redirect('/random_word')