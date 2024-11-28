from django.http import HttpResponse
from django.shortcuts import render

from testapp.models import UserData

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

# def hello(request):
#     return HttpResponse("Welcome To Web Application")

# def hii(request):
#     return HttpResponse("Welcome Again To Web Application")

def add(request):
    no1=request.GET['no1']
    no2=request.GET['no2']
    answer=int(no1)+int(no2)

    return  render(request,"testapp/templates/operation.html",{'answer':answer,'no1':no1,'no2':no2})

def giveMePage(request):
    return  render(request,'testapp/templates/operation.html')

def save(request):
    usernamefrombrowser=request.GET["username"]
    passwordfrombrowser=request.GET["password"]
    monofrombrowser=request.GET["mono"]

    UserData.objects.create(username=usernamefrombrowser,password=passwordfrombrowser,mono=monofrombrowser)

    return render(request,"testapp/templates/login.html",{'message':'Student Register Successfullly...'})

def giveMeRegister(request):
    return render(request,'testapp/templates/register.html')



# On the basis of API-
@api_view(['GET','POST'])
def getmestudinfo(request):
    return Response({'rno':101,'name':"Rohit"})