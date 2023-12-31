from xmlrpc.client import getparser
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-/|\,.<>?'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length =  int(request.GET.get('length',8))   
    genpass = ''

    for x in range(length):
        genpass+=random.choice(characters)
    return render(request,'generator/password.html', { 'password':genpass})

def about(request):
    return render(request,'generator/about.html')
