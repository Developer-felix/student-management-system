from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def showDemoPage(request):
    return render(request, 'demo.html')

def ShowLoginPage(request):
    return render(request, 'login_page.html')

#form data passing on form submit else error
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2 > Method Not Allowed </h2> ")
    else:
        return HttpResponse("Email :"+request.POST.get("email")+"Password :"+request.POST.get("password"))


        