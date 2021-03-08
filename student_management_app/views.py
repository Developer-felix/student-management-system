import datetime
from django.contrib import messages
# from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate ,login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from channels.auth import login , logout
from student_management_app.EmailBackEnd import EmailBackEnd

def showDemoPage(request):
    return render(request, 'demo.html')

def ShowLoginPage(request):
    return render(request, 'login_page.html')

#form data passing on form submit else error
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2 > Method Not Allowed </h2> ")
    else:
        user = EmailBackEnd.authenticate(request, username = request.POST.get("email"), password = request.POST.get("password"))
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/admin_home')
            # return HttpResponse("Email :" + request.POST.get("email") + "Password :" + request.POST.get("password"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User :" +request.user.email+ "usertype :" +request.user.user_type)
    else:
        return HttpResponse("Please login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

        