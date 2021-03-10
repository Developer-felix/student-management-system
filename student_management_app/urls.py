from django.urls import path
from . import views
from . import HodViews

urlpatterns = [
  path('darshbord', views.showDemoPage, name="demo"),
  path('', views.ShowLoginPage, name="login"),
  path('doLogin', views.doLogin),
  path('get_user_details', views.GetUserDetails),
  path('logout_user', views.logout_user),
  path('admin_home', HodViews.admin_home),
  path('add_staff/', HodViews.AddStaff),
  path('add_staff_save', HodViews.add_staff_save),
  path('add_course', HodViews.add_course),
  path('add_course_save', HodViews.add_course_save),
  path('add_student', HodViews.add_student),
  path('add_student_save', HodViews.add_student_save),
  path('add_subject', HodViews.add_subject),
  path('add_subject_save', HodViews.add_subject_save),
  path('manage_staff', HodViews.manage_staff),
   path('manage_student', HodViews.manage_student),
]
