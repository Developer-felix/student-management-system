import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser, Staffs, Courses, Student, Subject, Courses
from django.core.files.storage import FileSystemStorage

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
            # messages.success(request,"Successfully added Staff")
            messages.success(request,"Successfully added Staff")
            return HttpResponseRedirect("/add_staff")
            print("succcess")
        except:
            messages.error(request,"Failed to add Staff")
            return HttpResponseRedirect("/add_staff")
            print("succcess")

def add_course(request):
    return render(request, 'hod_template/add_course_template.html')

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Failed to add Course")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(request, 'hod_template/add_student_template.html',{"courses":courses})



def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allow")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")

        # profile_pic = request.FILES.get('profile_pic')
        # fs = FileSystemStorage()
        # filename = fs.save(profile_pic,profile_pic)
        # profile_pic_url = fs.url(filename)
        # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
        # if len(request.FILES) != 0:
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        # else:
        #     profile_pic_url = None
        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=3)
            user.student.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.student.course_id = course_obj
        # print(course_obj)
        # start_date = datetime.datetime.strptime(session_start,'%y-%m-%d').strftime('%Y-%m-%d')
        # end_date = datetime.datetime.strptime(session_end,'%y-%m-%d').strftime('%Y-%m-%d')

            user.student.session_start_year = session_start
            user.student.session_end_year = session_end
            user.student.gender = sex
            user.student.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add Student")
            return HttpResponseRedirect("/add_student")

def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=3)
    return render(request,'hod_template/add_subject_template.html',{"courses":courses, "staffs":staffs})

def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Method Not Allow </h2>" )
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
        try:
            subject = Subject(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Successfully added Subject")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request, "Failed to add Subject")
            return HttpResponseRedirect("/add_subject")

def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request, "hod_template/manage_staff_template.html", {"staffs": staffs})

def manage_student(request):
    students = Student.objects.all()
    return render(request, "hod_template/manage_student_template.html", {"students": students})

def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "hod_template/manage_course_template.html", {"courses": courses})

def manage_subject(request):
    subjects = Subject.objects.all()
    return render(request, "hod_template/manage_subject_template.html", {"subjects": subjects})

def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request, 'hod_template/edit_staff_template.html', {"staff": staff})

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
        
            staff_model = Staffs.objects.get(id=staff_id)
            staff_model.address = address
            staff_model.save()
            
            messages.success(request, "Successfully Edited the Staff")
            return HttpResponseRedirect("/edit_staff/"+staff_id)
        except:
            messages.error(request, "Failed to Editing the Staff")
            return HttpResponseRedirect("/edit_staff/" + staff_id)
            
def edit_student(request, student_id):
    courses = Courses.objects.all()
    student = Student.objects.get(admin=student_id)
    return render(request, 'hod_template/edit_student_template.html', {"student": student,"courses":courses})

def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        course_id = request.POST.get("course")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        sex = request.POST.get("sex")

        if len(request.FILES) != 0:
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
        
            student_model = Student.objects.get(admin=student_id)
            student_model.address = address
            student_model.gender = sex
            student_model.session_start = session_start
            student_model.session_end = session_end
            if profile_pic_url != None:
                student.profile_pic = profile_pic_url
            student_model.save()
            
            course = Courses.objects.get(id=course_id)
            student_model.course_id = course
            student_model.save()

            messages.success(request, "Successfully Edited the student")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.error(request, "Failed to Editing the student")
            return HttpResponseRedirect("/edit_student/" + student_id)

def edit_subject(request,subject_id):
    subjects = Subject.objects.get(id=subject_id)
    return render(request, 'hod_template/edit_subject_template.html', {"subjects":subjects})

def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")


def edit_course(request,course_id):
    course = Courses.objects.get(id=course_id)
    return render(request, 'hod_template/edit_course_template.html', {"course":course})


def edit_course_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()

            messages.success(request, "Course Updated Successfully.")
            return HttpResponseRedirect('/edit_course/'+course_id)

        except:
            messages.error(request, "Failed to Update Course.")
            return HttpResponseRedirect('/edit_course/'+course_id)
