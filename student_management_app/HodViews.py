from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser,Staffs

def admin_home(request):
    return render(request, 'hod_template/home_content.html')

def AddStaff(request):
    return render(request, 'hod_template/add_staff_template.html')


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allow")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request,"Successfully added Staff")
            return HttpResponseRedirect("/add_staff")
            print("succcess")
        except:
            messages.error(request,"Failed to add Staff")
            return HttpResponseRedirect("/add_staff")
            print("succcess")
        