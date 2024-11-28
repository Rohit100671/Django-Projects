from django.shortcuts import render
# Create your views here.

def result(request):
    no1=request.GET["no1"]
    no2=request.GET["no2"]
    opr=request.GET["op"]

    if opr == 'addition':
        answer=int(no1)+int(no2)
    
    elif opr== 'sub':
        answer=int(no1)-int(no2)

    elif opr == 'mul':
        answer=int(no1)*int(no2)
    
    else:
        answer=int(no1)/int(no2)
        
    
    return render(request,"calciapp/templates/opration.html",{"answer":answer, "no1":no1,"no2":no2})


def giveMeResult(request):
    return render(request,'calciapp/templates/opration.html')