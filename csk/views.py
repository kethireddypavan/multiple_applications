from django.shortcuts import render

# Create your views here.
def msd(request):
    return render(request,'msd.html')

from django.http import HttpResponse

def raina(request):
    return HttpResponse('<h1>mr 360</h1>')