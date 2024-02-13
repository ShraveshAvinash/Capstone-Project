from django.shortcuts import render,HttpResponseRedirect
from .forms import Patient_RegisterForm,Patient_LoginForm,Doctor_LoginForm,Doctor_RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from MediSyncHub.settings import EMAIL_HOST_USER

def home(request):
    return render(request,'mediTemp/index.html')

def about(request):
    return render(request='mediTemp/about.html')
#patient registration page 
def p_registration(request):
    if request.method == 'POST':
        fm=Patient_RegisterForm(request.POST)
        if fm.is_valid():
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            subject = f'Hey {first_name.capitalize()} {last_name.capitalize()} welcome to MediSyncHub'
            message = 'Thanks for Registering to MediSyncHub.\n You will soon awail all ther facilities of MediSync-Hub .' 
            recepient = str(fm['email'].value())
            send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            messages.success(request,'Registered Successfully')
          
            fm.save()
    else:
        fm=Patient_RegisterForm()
    return render(request,'mediTemp/p_registration.html',{'form':fm})

def d_registration(request):
    if request.method == 'POST':
        fm=Doctor_RegisterForm(request.POST)
        if fm.is_valid():
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            subject = f'Hey Dr. {first_name.capitalize()} {last_name.capitalize()} welcome to MediSyncHub'
            message = 'Thanks for Registering to MediSyncHub.\n You will soon awail all ther facilities of MediSync-Hub .' 
            recepient = str(fm['email'].value())
            send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            messages.success(request,'Registered Successfully')
          
            fm.save()
    else:
        fm=Patient_RegisterForm()
    return render(request,'mediTemp/d_registration.html',{'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=Patient_LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return HttpResponseRedirect('/patient_dashboard/')
        else:
            fm=Patient_LoginForm()
        return render(request,'mediTemp/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/patient_dashboard')
    
def doctor_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=Doctor_LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return HttpResponseRedirect('/doctor_dashboard/')
        else:
            fm=Patient_LoginForm()
        return render(request,'mediTemp/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/doctor_dashboard')

def about(request):
    return render(request,'mediTemp/about.html')



    
def user_logout(request):
    fm=logout(request)
    return HttpResponseRedirect('/')



def patient_dashboard(request):
    return render(request,'mediTemp/patient_dashboard.html')

def doctor_dashboard(request):
    return render(request,'mediTemp/doctor_dashboard.html')


