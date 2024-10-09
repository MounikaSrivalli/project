from django.http import HttpResponse
from django.shortcuts import render

def getHome(request):
    return render(request,"home.html")