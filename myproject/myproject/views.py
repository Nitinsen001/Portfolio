from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')     

def portfolio(request):
    return render(request, 'portfolio.html')     

def about(request):
    return render(request, 'about.html')     

def contact(request):
    return render(request, 'contact.html')     

def skills(request):
    return render(request, 'skill.html')



