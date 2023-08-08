from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(request):
    mensagem=''
    return render (request,'login.html')