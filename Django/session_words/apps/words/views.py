# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    try:
        request.session['words']
    except:
        print "Empty"
        request.session['words'] = []
    return render(request, 'words/index.html')

def add(request):
    if request.method == "POST":
        print request.POST
        if 'big' in request.POST:
            big = True
        else:
            big = False

        time = datetime.datetime.now().strftime('%I:%M:%S %p, %B %d, %Y')

        word_builder = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'big': big,
            'date': time
        }
        request.session['words'].append(word_builder)
        # print request.session['words']
        request.session.modified = True
        return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')