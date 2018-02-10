# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from aip import AipSpeech
from dictation.models import pronance_webster_mp3 as pwmp3
APP_ID = '10815485'
API_KEY = 'GZAu6jWx8d02zqKBpGekkk70'
SECRET_KEY = 'OjAgD3ggvBLYEDh4d49e7r2TbglOWyBD'

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def upload_file(request):
    if request.method == "POST":
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            with open("/tmp/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponseRedirect('/dictation/form/?filename=%s'%File.name);

    else:
        return render(request, 'dictation/upload_list.html')

def dictation_form(request):
    filename=request.GET['filename']
    context={}
    list=[]
    file = open("/tmp/%s" %filename)
    while 1:
        line = file.readline()
        if not line:
            break
        list.append(line)
    file.close()
    a=set(list)
    context={
        'words':a
    }
    return render(request, 'dictation/dictation_form.html', context)

def word_voice(request):
    word = request.GET['wordname']
    try:
        word_obj=pwmp3.objects.get(word_name=word)
        word_path = '/Users/tosnower/Desktop/mp3/%s' % (word_obj.word_path)
    except pwmp3.DoesNotExist:
        bath_path='%s/%s.mp3'%(word[0:1].upper(),word)
        word_path = '/Users/tosnower/Desktop/mp3/%s' % (bath_path)
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = client.synthesis(word, 'zh', 1, {
            'vol': 5,
        })
        if not isinstance(result, dict):
            with open(word_path, 'wb') as f:
                f.write(result)
        word_obj = pwmp3(word_name=word,word_path=bath_path)
        word_obj.save()


    # do something...
    with open(word_path, 'rb') as f:
        c = f.read()
    return HttpResponse(c)