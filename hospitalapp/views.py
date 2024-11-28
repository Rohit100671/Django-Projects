from django.shortcuts import render

from hospitalapp.models import DoctorData

# Create your views here.

def newregistration(request):
    if request.method == 'GET':
        return render(request,'hospitalapp/templates/register.html')
    
    doctorid=request.POST["id"]
    doctorname=request.POST["name"]
    doctordep=request.POST["dep"]
    doctormono=request.POST["mono"]

    try:
        DoctorData.objects.create(id=doctorid, name=doctorname, dep=doctordep, mono=doctormono)
    except:
        return render(request,'hospitalapp/templates/register.html',{'message':'Invalide Information Entered'})

    return render(request,'hospitalapp/templates/login.html',{'message':'Doctor Registration Successful...'})

def login(request):
    if request.method == 'GET':
        return render(request,'hospitalapp/templates/login.html')

    doctorid=request.POST["id"]
    doctorname=request.POST["name"]
    try:
        check=DoctorData.objects.get(id=doctorid)
    except:
        return render(request,'hospitalapp/templates/login.html',{'message':'Invalid Doctor Id'})
    

    if check.name == doctorname:
        return render(request,'hospitalapp/templates/welcome.html',{'message':'Welcome Doctor '+doctorname+', Welcome to RJT Hospital Management'})
    else:
        return render(request,'hospitalapp/templates/login.html',{'message':'Invalid Doctor Name'})



# To show all containt of database.
def doctorlist(request):
    doctordata=DoctorData.objects.all().values
    return render(request,'hospitalapp/templates/doctorlist.html',{'doctordata':doctordata})


# To view the given id Information in textbox.
def view(request):
    doctorid=request.POST["id"]
    doctordata=DoctorData.objects.get(id=doctorid)
    return render(request,'hospitalapp/templates/register.html',{'doctordata':doctordata})


# To Update the given id Information in textbox.
def update(request):
    doctorid=request.POST["id"]
    doctordata=DoctorData.objects.get(id=doctorid)
    doctordata.name=request.POST["name"]
    doctordata.dep=request.POST["dep"]
    doctordata.mono=request.POST["mono"]
    doctordata.save()
    return render(request,'hospitalapp/templates/register.html',{'message':'Record Update Successfully...'})


# To view the given id Information in textbox.
def delete(request):
    doctorid=request.POST["id"]
    doctordata=DoctorData.objects.filter(id=doctorid).delete()
    return render(request,'hospitalapp/templates/register.html',{'message':'Record Deleted Successfully...'})

#Contact Navbar Content.
def contact(request):
    return render(request,'hospitalapp/templates/contact.html')

# To Displya th emain hospital page.
def rjthospital(request):
    return render(request,'hospitalapp/templates/hospitalpage.html')