import json
from django.http import HttpResponse
from empregapp.models import EmpData

from django.shortcuts import render


# Create your views here.

def empregistration(request):
    if request.method == 'GET':
        return render(request, 'empregapp/templates/empregister.html')

    employee_id=request.POST["empid"]
    employee_name=request.POST["empname"]
    employee_dep=request.POST["empdep"]
    employee_mono=request.POST["empmono"]
    try:
        EmpData.objects.create(empid=employee_id, empname=employee_name, empdep=employee_dep, empmono=employee_mono)
    except:
         return render(request,'empregapp/templates/empregister.html',{'emptymessage':'Invalid Inputs! please try Again...'})


    return render(request,'empregapp/templates/empregister.html',{'emptymessage':'Registration successful...Welcome To RJT pvt.Ltd.'})


# def table(request):
#     getalltabledata=EmpData.objects.all().values()
#     return render(request,'empregapp/templates/table.html',{'getalltabledata':getalltabledata})

# CRUD Operations in Employee Registration.

def view(request):
    employee_id=request.GET["empid"]
    try:
        empdata=EmpData.objects.get(empid=employee_id)
    except:
        return render(request,'empregapp/templates/empregister.html',{'emptymessage':'Your Record does not Exist'})
    

    return render(request,'empregapp/templates/empregister.html',{'empdata':empdata})



def remove(request):
    employee_id=request.GET["empid"]
    EmpData.objects.filter(empid=employee_id).delete()
    return render(request,'empregapp/templates/empregister.html',{'emptymessage':'Your Record has been Deleted'})

def update(request):
    employee_id=request.GET["empid"]
    empdata=EmpData.objects.get(empid=employee_id)
    empdata.empname=request.GET["empname"]
    empdata.empdep=request.GET["empdep"]
    empdata.empmono=request.GET["empmono"]
    empdata.save()

    return render(request,'empregapp/templates/empregister.html',{'emptymessage':'Record has Update Successfull'})




def login(request):
    if request.method == 'GET':
        return render(request, 'empregapp/templates/login.html')

    employee_id=request.POST["empid"] 
    employee_name=request.POST["empname"] 

    try:
        check=EmpData.objects.get(empid=employee_id) 
    except:
        return render(request, 'empregapp/templates/login.html', {'deploginmessage':'Employee ID and Name does not Exist! Please try again...'})

    if  check.empname == employee_name:
        return render(request,'empregapp/templates/welcome.html',{'welcomemessage':'Hello ' + employee_name + ' Welcome to RJT Pvt.Ltd.'})
    
    else:
        return render(request,'empregapp/templates/login.html',{'deploginmessage':'Your EmployeeName does not Exist! Failed! Please Try again...'})


# def giveMeEmployee(request):
#     return render(request,'empregapp/templates/empregister.html')



def check(request):
    employee_id=request.GET["empid"] 
    message="Employee ID Already Exists"
    try:
        EmpData.objects.get(empid=employee_id)
    except:
        message="Employee ID is Valide"

    dictionary={'message':message}
    jsondata=json.dumps(dictionary)

    response=HttpResponse(f'{jsondata}', content_type='application/json')
    return response
