from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rcbcaptain(request):
    return HttpResponse('RCB captain is VIRAT KOHLI')