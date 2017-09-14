# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context=helpdict)