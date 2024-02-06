from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

class Patient_RegisterForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    password2=forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','phone_no','address']
        labels ={'username':'Username', 'first_name':'First Name', 'last_name':'Last Name', 'email':'Email','phone_no':'Phone-no','address':'Address'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                'first_name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                'last_name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                'email':forms.EmailInput(attrs={'class':'form-control form-control-sm'}),
                'phone_no': PhoneNumberPrefixWidget(initial='CA'),
                'address': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                }

class Patient_LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control form-control-sm'}))
    password=forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control form-control-sm'}))
    
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','phone_no','address']
        labels ={'username':'Username', 'first_name':'First Name', 'last_name':'Last Name', 'email':'Email','phone_no':'Phone-no','address':'Address'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                'first_name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                'last_name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                'email':forms.EmailInput(attrs={'class':'form-control form-control-sm'}),
                'phone_no': PhoneNumberPrefixWidget(initial='CA'),
                'address': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
               
                }


