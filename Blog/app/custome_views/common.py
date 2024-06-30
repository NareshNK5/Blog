from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import *
from app.serializers.serializer import Tbluserserializer
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
def registerUserSave(request):
    print('registerUserSave')
    if request.method=='POST':
        serializeData = Tbluserserializer(data = request.data)
        if serializeData.is_valid():
            serializeData.save()
            return Response({'data':'Login Successfully'},template_name='layout/login.html')
        return Response({'data':'success'},template_name='layout/register.html')
    return Response({'data':'success'},template_name='layout/register.html')