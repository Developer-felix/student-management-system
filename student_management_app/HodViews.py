from django.shortcuts import render

def admin_home(request):
    return render(request, 'hod_template/home_content.html')

def AddStaff(request):
    return render(request,'hod_template/add_staff_template.html')