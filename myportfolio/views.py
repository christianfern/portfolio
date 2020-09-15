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
import os

from myportfolio.classes.POPO import Word, CodeFile

def index(request):
    return render(request, 'myportfolio/start.html')

def about_me(request):
    return render(request, 'myportfolio/about-me.html')

def demos(request):
    return render(request, 'myportfolio/demos.html')

def experience(request):
    return render(request, 'myportfolio/experience.html')

def processing_demo(request):
    files = retrieve_files(settings.SCRIPTS_DIR, ['sorting-alg-demo.pde','main-script.js'])
    return render(request, 'myportfolio/processing-demo.html', {'files': files})

def definitions_api_demo(request):
    return render(request, 'myportfolio/definitions-api-demo.html')

def owlbot_api_get_word(word):
    headers = {'Authorization': settings.OWLBOT_TOKEN}
    response = requests.get('https://owlbot.info/api/v4/dictionary/{}'.format(word), headers=headers)
    data = json.dumps(response.json())
    myWord = json.loads(data, object_hook=lambda d: namedtuple('Word', d.keys())(*d.values()))
    return myWord

def testPost():
    print('Entered')

def definitions_api_demo_response(request):
    word_json = None
    if request.method == "GET":
        MyDefinitionLookupForm = DefinitionLookupForm(request.GET)
        if MyDefinitionLookupForm.is_valid():
            my_word = MyDefinitionLookupForm.cleaned_data['word']
            word_json = owlbot_api_get_word(my_word)
    files = retrieve_files(settings.MYPORTFOLIO_ROOT, ['views.py'])
    return render(request, 'myportfolio/definitions-api-demo-response.html', {'word_json': word_json, 'files': files})

def retrieve_files(base_dir, file_name_list):
    files = []
    for file_name in file_name_list:
        f = open(os.path.join(base_dir + file_name), 'r')
        file_content = f.read()
        code_file = CodeFile(file_name, file_content)
        files.append(code_file)
        f.close()
    return files

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)