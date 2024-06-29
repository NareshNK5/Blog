from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import *
from app.serializers.serializer import Tbluserserializer
from django.views.decorators.csrf import csrf_exempt
@api_view(['GET','POST'])
def home(request):
    print('home')
    if request.method=='GET':
        return Response({'data':''},template_name='layout/home.html')
    return Response({'data':'success'},template_name='layout/home.html')

@api_view(['GET','POST'])
def loginPage(request):
    print('loginPage')
    if request.method=='GET':
        return Response({'data':''},template_name='layout/login.html')
    return Response({'data':'success'},template_name='layout/login.html')

@api_view(['GET','POST'])
def registerPage(request):
    print('registerPage')
    if request.method=='GET':
        return Response({'data':''},template_name='layout/register.html')
    return Response({'data':'success'},template_name='layout/register.html')

@api_view(['GET','POST'])
def registerUserSave(request):
    print('registerUserSave')
    if request.method=='POST':
        serializeData = Tbluserserializer(data = request.data)
        if serializeData.is_valid():
            serializeData.save()
            return Response({'data':'Login Successfully'},template_name='layout/login.html')
        return Response({'data':'success'},template_name='layout/register.html')
    return Response({'data':'success'},template_name='layout/register.html')