from django.shortcuts import render

# Create your views here.

def login(request):
    username=request.GET["username"]
    password=request.GET["password"]

    return render(request,'loginapp/templates/login.html',{'username':username,'password':password})

def giveMeLogin(request):
        return render(request,'loginapp/templates/login.html')
