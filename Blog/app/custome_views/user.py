from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from app.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from app.serializers.serializer import *


def loginCheck(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if Tbluser.objects.filter(username=username,password=password).exists():
            request.session['user'] = username
            return render(request,'layout/home.html',{"user":username})
        return HttpResponseRedirect('/api/loginPage')


def userBlog(request):
    if request.session.has_key("user"):
        un = request.session['user']
        name = Tbluser.objects.get(username=un)
        uid = name.id
        post=Tblpost.objects.all()
        return render(request,'user/userBlog.html',{"post":post,'user':un,'uid':uid})

@api_view(["POST"])
def userBlogPost(request):
    if request.session.has_key("user"):
        un = request.session['user']
        name = Tbluser.objects.get(username=un)
        if request.method=="POST":
            serializeData={}
            serializeData["author"] = name
            serializeData = Tblpostserializer(data = request.data)
            if serializeData.is_valid():
                serializeData.save()
                return Response(serializeData.data,status=status.HTTP_200_OK)
            return Response(serializeData.error,status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponseRedirect('/api/loginPage/')
    
@api_view(["GET"])
def userBlogView(request):
    if request.method=="GET":
        print("education list")
        post=Tblpost.objects.all()
        serializer=Tblpostserializer(post,many=True)
        # print(educate)
        return Response(serializer.data)