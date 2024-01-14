from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    return render(request, 'generator/index.html')
def about(request):
    return render(request,'generator/about.html')
def password(request):
    char=list(' ')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('lowercase'):
        char.extend(list('abcdefghijklmnopqrstuvwxzy'))

    if request.GET.get('numbers'):
        char.extend(list('1234567890'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length',12))

    password = ''
    for x in range(length):
        password += random.choice(char)

    return render(request, 'generator/password.html',{'password':password})
