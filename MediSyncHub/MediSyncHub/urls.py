"""MediSyncHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from MediSyncApp import views
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',views.home,name='hm'),
    path('p_registration/',views.p_registration,name='p_registration'),
    path('user_login/',views.user_login,name='login'),
    path('d_registration/',views.d_registration,name='d_registration'),
    path('doctor_login/',views.doctor_login,name='d_login'),
    path('about/',views.about,name='about'),
    path('patient_dashboard/',views.patient_dashboard,name='patient_dashboard'),
    path('doctor_dashboard/',views.doctor_dashboard,name='doctor_dashboard'),
    path('logout/',views.user_logout,name='logout')
]
