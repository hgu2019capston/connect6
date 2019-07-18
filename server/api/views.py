from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics

from .models import *
from .serializers import *

from django.http import Http404, HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random, requests, time
from django.conf import settings
from string import ascii_uppercase
from django.urls import reverse
from rest_framework.viewsets import ModelViewSet

from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.decorators import api_view
import threading

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def index(request):
    colorNum = random.randrange(1,3)
    if colorNum == 1:
        color = "white"
    else :
        color = "black"
    
    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)

    if session_key is None:
        request.session.set_test_cookie()
        return render(request, 'index.html', {'session_key':"No Session ID, refresh page!"})

    elif Session.objects.filter(session_name=session_key).exists():
        s = Session.objects.get(session_name=session_key)
#        return render(request, 'index.html', {'session_key':s.id, "color":color})
    
    else: 
        s = Session(session_name = str(session_key), color=color)
        s.save()

        if s.color == "white":
            x = random.choice('ABCDEFGHIJKLMNOPQRS')
            y = random.randrange(1,20)
            data = {'room': s.id, 'color': "black" , 'x1': x, 'y1': y, 'x2': '', 'y2': 0}
            requests.post('http://turnincode.cafe24.com:8880/home/sessions/'+str(s.id)+'/stones/', data=data)

    return render(request, 'index.html', {'session_key':s.id, "color":s.color})

def getSession(request):
    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
    s = Session.objects.get(session_name=session_key)
    return JsonResponse(str(s.id), safe=False)

class SessionViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

def gameover():
    print("game over")

class StoneViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = StoneSerializer
    queryset = Stone.objects.all()

    def get_queryset(self):
        time=threading.Timer(7, gameover)
        time.start()
        session_key = self.request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        s = Session.objects.get(session_name=session_key)
        return Stone.objects.filter(room=s.id)


def ResultData(request, pk):
    
    tmp = ResultOmok.objects.filter(room=pk)
    black = tmp.filter(color="black")
    white = tmp.filter(color="white")

    bCount = black.count()
    wCount = white.count()
    
    row = list(ascii_uppercase)

    for i in row:
        for j in range(1,20):
            if tmp.filter(color="black",x=i, y=j).count() == 1:
                cnt=1
                for jj in range(1, 6):
                    if tmp.filter(color="black",x=i, y=j+jj).count() == 1:
                        cnt+=1
                if cnt == 6:
                    result = str('Black WIN !!! ')
                    return JsonResponse(result , safe = False)
                else:
                    cnt =0
            elif tmp.filter(color="white",x=i, y=j).count() == 1:
                cnt=1
                for jj in range(1, 6):
                    if tmp.filter(color="white",x=i, y=j+jj).count() == 1:
                        cnt+=1
                if cnt == 6:
                    result = str('White WIN !!! ')
                    return JsonResponse(result , safe = False)
                else:
                   cnt=0

    for j in range(1,20):
        for i in row:
            if black.filter(x=i, y=j).count() == 1:
                cnt = 1
                for jj in range(1, 6):
                    if black.filter(x=chr(ord(i)+jj), y=j).count() == 1:
                        cnt +=1
                if cnt == 6:
                    result = str('Black WIN !!!! ')

                    return JsonResponse(result, safe = False)
                else:
                    cnt =0
            elif white.filter(x=i, y=j).count() == 1:
                cnt = 1
                for jj in range(1,6):
                    if white.filter(x=chr(ord(i)+jj), y=j).count() == 1:
                        cnt +=1
                if cnt == 6:
                    result = str('White WIN !!!! ')
                    return JsonResponse(result, safe = False)
                else:
                    cnt =0


    for i in range(1,20):
        for j in row:
            if black.filter(x=j, y=i).count() == 1:
                cnt = 1
                for jj in range(1,6):
                    if tmp.filter(color="black", x=chr(ord(j)+jj) , y = i+jj).count()==1:
                        cnt+=1
                if cnt == 6:
                    result = str('Black WIN !!! ')
                    return JsonResponse(result, safe=False)
                else:
                    cnt = 0
            if white.filter(x=j, y=i).count() == 1:
                cnt = 1
                for jj in range(1,6):
                    if tmp.filter(color="white", x=chr(ord(j)+jj) , y = i+jj).count()==1:
                        cnt+=1
                if cnt == 6:
                    result = str('White WIN !!! ')
                    return JsonResponse(result, safe=False)
                else:
                    cnt = 0


    for i in row:
        for j in range(1,20):
            if black.filter(x=i, y=j).count() == 1:
                cnt = 1
                for jj in range(1,6):
                    if tmp.filter(color="black", x=chr(ord(i)+jj) , y = j-jj).count()==1:
                        cnt+=1
                if cnt == 6:
                    result = str('Black WIN !!! ')
                    return JsonResponse(result, safe=False)
                else:
                    cnt = 0
            if white.filter(x=i, y=j).count() == 1:
                cnt = 1
                for jj in range(1,6):
                    if tmp.filter(color="white", x=chr(ord(i)+jj) , y = j-jj).count()==1:
                        cnt+=1
                if cnt == 6:
                    result = str('White WIN !!! ')
                    return JsonResponse(result, safe=False)
                else:
                    cnt = 0


    return HttpResponse()
