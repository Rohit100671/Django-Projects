import json
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from registerapp.models import UserData
from registerapp.models import Employee
from django.db.models import Sum, Avg, Count, Max, Min

# Create your views here.

def save(request):
    if request.method == 'GET':
        return render(request,'registerapp/templates1/register.html')

    userfrombrowser=request.POST["username"]
    passwordfrombrowser=request.POST["password"]
    monofrombrowser=request.POST["mono"]

    try:
        UserData.objects.create(username=userfrombrowser,password=passwordfrombrowser,mono=monofrombrowser)
    except:
        if  userfrombrowser== '':
            return render(request,'registerapp/templates1/register.html',{'message':'Invalid Entered Data! Please try again...'})

    return render(request,'registerapp/templates1/login.html',{'message':'User Register Successful...'})

def login(request):
    if request.method == 'GET':
        return render(request,'registerapp/templates1/login.html')

    userfrombrowser=request.POST["username"]
    passwordfrombrowser=request.POST["password"]

    try:
        check=UserData.objects.get(username=userfrombrowser)
    except:
        return render(request,'registerapp/templates1/login.html',{'invalidmessage':'Entered UserName Invalid'})
    
    if check.password == passwordfrombrowser:
        return render(request,'registerapp/templates1/messages.html',{'loginmessage':'User login successful ' + ' Welcome...... ' + userfrombrowser})
    
    else:
        return render(request,'registerapp/templates1/login.html',{'invalidmessage':'Your Account do not present'})
     

# def giveMeRegister(request):
#     return render(request,'registerapp/templates1/register.html')


def getallusers(request):
    allusers=UserData.objects.all().values()

    return render(request, 'registerapp/templates1/display.html',{'getallusers':allusers})

def delete(request,userfrombrowser):
    UserData.objects.filter(username=userfrombrowser).delete()
    UserData.objects.all().values()
    return getallusers(request)



# CRUD Operation on web page.

def view(request):
    userfrombrowser=request.GET["username"]
    
    try:  
        userdata=UserData.objects.get(username=userfrombrowser)
    except:
        return render(request,'registerapp/templates1/crud.html',{'message':'Record not Exist'})
    
    return render(request,'registerapp/templates1/crud.html',{'userdata':userdata})
    

def add(request):
    userfrombrowser=request.GET["username"]
    passwordfrombrowser=request.GET["password"]
    monofrombrowser=request.GET["mono"]
    try:
        UserData.objects.create(username=userfrombrowser,password=passwordfrombrowser,mono=monofrombrowser)
    except:
        return render(request,'registerapp/templates1/crud.html',{'message':'Record Already Exist'})

    return render(request,'registerapp/templates1/crud.html')

def remove(request):
    userfrombrowser=request.GET["username"]
    UserData.objects.filter(username=userfrombrowser).delete()
    return render(request,'registerapp/templates1/crud.html',{'message':'Record has Deleted'})

def update(request):
    userfrombrowser=request.GET["username"]
    userdata=UserData.objects.get(username=userfrombrowser)
    userdata.password=request.GET["password"]
    userdata.mono=request.GET["mono"]
    userdata.save()

    return render(request,'registerapp/templates1/crud.html',{'message':'Record has Update Successfull'})


# def showdata(request):
#     userfrombrowser=request.GET["username"]  
#     userdata=UserData.objects.get(username=userfrombrowser)
#     return render(request,'registerapp/templates1/table.html',{'userdata':userdata})
    



def giveMecrud(request):
    return render(request,'registerapp/templates1/crud.html')


def setsession(request):
    request.session["index"]=0  
    request.session["username"]='python'
    return HttpResponse("session is set")

def increase(request):
    request.session["index"]=request.session["index"]+1
    return HttpResponse(f"Index value is {request.session['index']}")


def check(request):
    userfrombrowser=request.GET["username"]
    message="UserName Already Present"
    try:
        UserData.objects.get(username=userfrombrowser)
    except:
        message="UserName is Valide"

    dictionary={'message':message}
    jsondata=json.dumps(dictionary)
    print(jsondata)

    response=HttpResponse(f'{jsondata}', content_type='application/json')
    return response


def getuser(request):
    # empdata=Employee.objects.filter(esalary__lt=250000)
    # empdata=Employee.objects.filter(esalary__range=(250000,300000))
    # empdata=Employee.objects.filter(esalary__isnull=True)
    # empdata=Employee.objects.aggregate(Max('esalary'))
    # empdata=Employee.objects.aggregate(Sum('esalary'))
    empdata=Employee.objects.aggregate(Count('esalary'))

    print(empdata)
    # print(connection.queries)
   
    return render(request,'registerapp/templates1/getuser.html',{'empdata':empdata})