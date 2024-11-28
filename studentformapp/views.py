from django.shortcuts import render

from studentformapp.models import StudentForm

# Create your views here.


def registerform(request):
    if request.method == 'GET':
        return render(request,'studentformapp/templates/registernew.html')
    
    username=request.POST["username"]
    password=request.POST["password"]
    email=request.POST["email"]
    mono=request.POST["mono"]
    filedata=request.FILES["photo"]
    imagepath='/upload/'+filedata.name

    with open('studentformapp/static/upload/'+filedata.name, 'wb+') as destination:
        for byte in filedata.chunks():
            destination.write(byte)

    StudentForm.objects.create(username=username, password=password, email=email, mono=mono, imagepath=imagepath)

    return render(request,'studentformapp/templates/loginnew.html',{'message':'LogIn Succusseful... Please LogIN Now'})

def loginnew(request):
    if request.method == 'GET':
        return render(request,'studentformapp/templates/loginnew.html')
    
    username=request.POST['username']
    password=request.POST['password']
    try:
        check=StudentForm.objects.get(username=username)
    except:
        return render(request,'studentformapp/templates/loginnew.html',{'message':"Invalid Username"})

    if check.password == password:
        imagepath=check.imagepath

        return render(request,'studentformapp/templates/welcomenew.html',{'message':"Welcome " +username+" Your LogIn Successfull", "imagepath":imagepath})
    else:
        return render(request,'studentformapp/templates/loginnew.html',{'failmessage':"Student LogIn Failed!  Please Try Again"})