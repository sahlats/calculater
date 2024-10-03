"""
URL configuration for calculater project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.AdditionView.as_view(),name="addition"),
    path('sub/',views.SubView.as_view()),
    path('multi/',views.MultiView.as_view()),
    path('div/',views.DivView.as_view()),
    path('perfect/',views.PerfectView.as_view()),
    path('arm/',views.ArmView.as_view()),
    path('emi/',views.EmiView.as_view(),name="emi"),
    path('bmi/',views.BmiView.as_view(),name="bmi"),
    path('calorie/',views.CalorieView.as_view(),name="calorie"),
    path('caloriemanage/',views.CalorieManageView.as_view(),name="calorie-manage"),
    path("",views.IndexView.as_view())




]
