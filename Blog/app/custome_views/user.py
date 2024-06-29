from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from app.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


def loginCheck(request):
    if request.method=="POST":
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = Tbluser.objects.filter(username=username,password=password).exists()
        print('user',user)
        if user is not None:
        # if Tbluser.objects.filter(username=username,password=password).exists():
            login(request,user)
            request.session['user'] = username
            print(request.session['user'])
            return JsonResponse({'redirect_url': '/api/home/'})
        return Response({'data':'invalid data'},template_name='layout/register.html')

    