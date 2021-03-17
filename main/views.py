from django.shortcuts import render

def Standart(request):
    return render(request, 'main/main.html')

def About(request):
    return render(request, 'main/about.html')

def Contact(request):
    return render(request, 'main/contacs.html')
