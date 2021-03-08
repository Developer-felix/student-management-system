from django.shortcuts import render


def showDemoPage(request):
    return render(request, 'demo.html')

def ShowLoginPage(request):
    return render(request, 'login_page.html')

def doLogin(request):
    pass