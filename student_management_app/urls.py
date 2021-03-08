from django.urls import path
from . import views

urlpatterns = [
  path('darshbord', views.showDemoPage, name="demo"),
  path('', views.ShowLoginPage, name="login"),
  path('doLogin',views.doLogin)
]
