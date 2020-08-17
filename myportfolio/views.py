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
from myportfolio.forms import DefinitionLookupForm

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
    return render(request, 'myportfolio/definitions-api-demo.html')

def owlbot_api_get_word(word):
    headers = {'Authorization': settings.OWLBOT_TOKEN}
    response = requests.get('https://owlbot.info/api/v4/dictionary/{}'.format(word), headers=headers)
    data = json.dumps(response.json())
    myWord = json.loads(data, object_hook=lambda d: namedtuple('Word', d.keys())(*d.values()))
    #for definition in myWord.definitions:
        #if definition.example != None:
            #definition.example = remove_html_tags(definition.example)
    return myWord

def testPost():
    print('Entered')

def definitions_api_demo_response(request):
    wordJson = None

    if request.method == "GET":
        MyDefinitionLookupForm = DefinitionLookupForm(request.GET)
        if MyDefinitionLookupForm.is_valid():
            myWord = MyDefinitionLookupForm.cleaned_data['word']
            wordJson = owlbot_api_get_word(myWord)
    return render(request, 'myportfolio/definitions-api-demo-response.html', {'wordJson': wordJson})

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)