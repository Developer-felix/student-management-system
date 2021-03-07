from django.shortcuts import render


def showDemoPage(request):
    return render(request,'demo.html')