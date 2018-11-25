from django.http import HttpResponse
from django.shortcuts import render




def homepage(req):
    return render(req,'home.html',)

def count(req):
    return render(req,'count.html')
