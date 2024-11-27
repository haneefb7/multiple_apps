from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def cskcaptain(request):
    return HttpResponse('csk captain is ruturaj gaikwad')