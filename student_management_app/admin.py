from django.contrib import admin

from .models import AdminHOD,Attendance,Courses,Staffs,Subject,Student,NotificationStaffs,NotificationStudent,LeaveReportStaffs,LeaveReportStudent,FeedBackStaffs,FeedBackStudent,AttendanceReport

admin.site.register(AdminHOD)
admin.site.register(Attendance)
admin.site.register(Courses)
admin.site.register(Staffs)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaffs)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(AttendanceReport)