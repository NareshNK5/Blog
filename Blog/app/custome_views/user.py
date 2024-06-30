from django.shortcuts import render,get_object_or_404
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
def userBlogPost(request,id):
    if request.session.has_key("user"):
        un = request.session['user']
        name = Tbluser.objects.get(username=un)
        print(id)
        if request.method=="POST":
            if id==0:
                serializeData={}
                serializeData["author"] = name
                serializeData = Tblpostserializer(data = request.data)
                if serializeData.is_valid():
                    serializeData.save()
                    return Response(serializeData.data,status=status.HTTP_200_OK)
                return Response(serializeData.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                print("blog edit")
                # serializeData={}
                # serializeData["author"] = name
                obj=get_object_or_404(Tblpost,id=id)
                serializeData = Tblpostserializer(obj,data = request.data)
                if serializeData.is_valid():
                    print("valid")
                    serializeData.save()
                    return Response(serializeData.data,status=status.HTTP_200_OK)
                print("Invalid")
                return Response(serializeData.errors,status=status.HTTP_400_BAD_REQUEST)
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

def blogPostImage(request):
    if request.method == "POST":
        id = request.POST["post"]
        file = request.FILES["images"]
        obj = Tblpost.objects.get(id=id)
        obj.images=file
        obj.save()
        return HttpResponseRedirect('/api/userBlog/')

@api_view(['GET'])
def blogEdit(request,id):
    print('blog edit')
    edu_list = get_object_or_404(Tblpost,id=id)
    serialize = Tblpostserializer(edu_list,many=False)
    return Response(serialize.data)