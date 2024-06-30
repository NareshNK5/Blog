from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
from app.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from app.serializers.serializer import *
from django.db.models import Avg


def loginCheck(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if Tbluser.objects.filter(username=username,password=password).exists():
            request.session['user'] = username
            return HttpResponseRedirect('/api/home/')
        return HttpResponseRedirect('/api/loginPage')

def userBlog(request):
    if request.session.has_key("user"):
        un = request.session['user']
        name = Tbluser.objects.get(username=un)
        uid = name.id
        post=Tblpost.objects.filter(author=name)
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
    if request.session.has_key("user"):
        un = request.session['user']
        name = Tbluser.objects.get(username=un)
        if request.method=="GET":
            post=Tblpost.objects.filter(author=name)
            serializer=Tblpostserializer(post,many=True)
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
    data = get_object_or_404(Tblpost,id=id)
    serialize = Tblpostserializer(data,many=False)
    return Response(serialize.data)

# @api_view(['POST'])
def blogSearch(request):
    if request.session.has_key("user"):
        un = request.session['user']
        if request.method == "POST":
            title = request.POST["key"]
            obj = Tblpost.objects.get(title = title)
            rate = Tblrate.objects.filter(post=obj).aggregate(Avg('rating'))
            print(rate)
            return render(request,'user/singleBlog.html',{"data":obj,'user':un,"average_rating":rate})
        
def blogViewOne(request,id):
    if request.session.has_key("user"):
        un = request.session['user']
        obj = Tblpost.objects.get(id = id)
        rate = Tblrate.objects.filter(post=obj).aggregate(Avg('rating'))
        return render(request,'user/singleBlog.html',{"data":obj,'user':un,"average_rating":rate})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@api_view(["GET"])
def blogdelete(request,id):
    print("test")
    if is_ajax(request=request):
        print("blog delete")
        bloglist = get_object_or_404(Tblpost,id=id)
        bloglist.delete()
        return Response("Deleted",status=status.HTTP_200_OK)
    else:
        return Response("Not Deleted",status=status.HTTP_400_BAD_REQUEST)
    
def blograting(request,id):
    if request.session.has_key("user"):
        un = request.session['user']
        user = Tbluser.objects.get(username = un)
        post = Tblpost.objects.get(id=id)
        if Tblrate.objects.filter(author=user,post=post).exists():
            return render(request,'user/singleBlog.html',{"data":post,'user':un,"msg":"Already you rated"})
        else:
            rate = request.POST["rating"]
            obj = Tblrate()
            obj.author=user
            obj.post=post
            obj.rating=rate
            obj.save()
            return HttpResponseRedirect('/api/home/')
        