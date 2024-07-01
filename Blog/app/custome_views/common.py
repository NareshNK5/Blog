from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app.models import *
from app.serializers.serializer import Tbluserserializer,Tblpostserializer
from django.core.paginator import Paginator

@api_view(['GET','POST'])
def home(request):
    post_list = Tblpost.objects.all().order_by("publication_date")
    paginator = Paginator(post_list, 10)  # 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.session.has_key("user"):
        un = request.session['user']
        return render(request,"layout/home.html",{"page_obj":page_obj,'user':un})
    return render(request,"layout/home.html",{"page_obj":page_obj,'user':"none"})
    

@api_view(['GET','POST'])
def loginPage(request):
    print('loginPage')
    if request.method=='GET':
        return Response({'data':'','user':"none"},template_name='layout/login.html')
    return Response({'data':'success'},template_name='layout/login.html')

@api_view(['GET','POST'])
def registerPage(request):
    print('registerPage')
    if request.method=='GET':
        return Response({'data':'','user':"none"},template_name='layout/register.html')
    return Response({'data':'success'},template_name='layout/register.html')

@api_view(['GET','POST'])
def registerUserSave(request,id):
    print('registerUserSave')
    if request.method=='POST':
        if id==0:
            serializeData = Tbluserserializer(data = request.data)
            if serializeData.is_valid():
                serializeData.save()
                return Response({'data':'Login Successfully'},template_name='layout/login.html')
            return Response({'data':'success'},template_name='layout/register.html')
        else:
            print("user edit")
            obj=get_object_or_404(Tbluser,id=id)
            serializeData = Tbluserserializer(obj,data = request.data)
            if serializeData.is_valid():
                print("valid")
                serializeData.save()
                return Response(serializeData.data,status=status.HTTP_200_OK)
            print("Invalid")
            return Response(serializeData.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'data':'success'},template_name='layout/register.html')

@api_view(["GET"])
def userProfile(request):
    if request.session.has_key("user"):
        un = request.session["user"]
        return Response({"data":"","user":un},template_name="user/profile.html")

@api_view(["GET"])
def userProfileGet(request):
    if request.session.has_key("user"):
        un = request.session["user"]
        data = get_object_or_404(Tbluser,username=un)
        serialize = Tbluserserializer(data,many=False)
        return Response(serialize.data)
    