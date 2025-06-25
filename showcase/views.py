from django.shortcuts import render

def homepage(request):
    return render(request,'showcase/home.html')

def aboutpage(request):
    return render(request,'showcase/about.html')


