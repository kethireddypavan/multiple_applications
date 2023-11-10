from django.shortcuts import render

def rohit(request):
    return render(request,'rohit.html')

from django.http import HttpResponse

def sky(request):
    return HttpResponse('sky is best t20 batter')