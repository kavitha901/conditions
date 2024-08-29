from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':10000,'b':200,'c':3000}
    return render(request,'conditions.html',d)

def loop(request):
    d={'name':'kavitha','mobile':[9014,8008]}
    return render(request,'loop.html',d)
