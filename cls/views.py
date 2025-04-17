from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def result(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    if 'add' in request.POST:
        res=n1+n2
    if 'sub' in  request.POST:
        res=n1-n2 
    if 'mul' in  request.POST:
        res=n1*n2 
    if 'div' in  request.POST:
        res=n1/n2 
    if 'mod' in  request.POST:
        res=n1%n2 
    return render(request,"result.html",{'res':res})