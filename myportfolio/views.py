from __future__ import unicode_literals

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import requests
import json
from collections import namedtuple
from django.conf import settings

from myportfolio.classes.Word import Word

def index(request):
    return render(request, 'myportfolio/start.html')

def about_me(request):
    return render(request, 'myportfolio/about-me.html')

def demos(request):
    return render(request, 'myportfolio/demos.html')

def processing_demo(request):
    return render(request, 'myportfolio/processing-demo.html')

def definitions_api_demo(request):
    word = "break"
    myWord = owlbot_api_get_word(word)
    return render(request, 'myportfolio/definitions-api-demo.html', {'myWord': myWord})

def owlbot_api_get_word(word):
    headers = {'Authorization': settings.OWLBOT_TOKEN}
    response = requests.get('https://owlbot.info/api/v4/dictionary/{}'.format(word), headers=headers)
    data = json.dumps(response.json())
    myWord = json.loads(data, object_hook=lambda d: namedtuple('Word', d.keys())(*d.values()))
    return myWord