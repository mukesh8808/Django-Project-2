from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import re
from django.contrib import messages
# Create your views here.

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    if (re.fullmatch(regex,email)):
        return True
    else:
        return False

def Check_Student(email, password):
    list1 = ['student1@gmail.com', 'student2@rediffmail.com', 'aman@yahoomail.com']
    list2 = ['asif@123', 'boby6753', '7hdjk972nd']
    value = zip(list1,list2)
    for data in list(value):
        if data[0] == email and data[1] == password:
            print('Student login')


def Check_Employee(email,password):
    list1 = ['asif@vercel.com', 'boby@arivani.net', 'aman@gmail.com']
    list2 = ['asif@123', 'boby6753', '7hdjk972nd']
    value = zip(list1,list2)
    for data in list(value):
        if data[0] == email and data[1] == password:
            print('Employees login')
    Check_Student(email, password)

def Check_Company(email,password):
    list1 = ['arivani@it.com', 'infotech@yogis.co', 'vercel@dotnet.net']
    list2 = ['ityogis@10#01!', 'info@g0n9qw12', '7hdjk972nd']
    value = zip(list1,list2)  
    for data in list(value):
        if email == data[0] and password == data[1]:
            print('Company login')
            # return redirect('/company/')
    Check_Employee(email,password)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # print(email)
        if not email:
            messages.error(request,"Please enter email!")
            return HttpResponseRedirect('/')
        check_email_valid = check(email)
        if not check_email_valid:
            messages.error(request,"Invalid email!")
            return HttpResponseRedirect('/')
        password = request.POST.get('password')
        if not password:
            messages.error(request,"Please enter password!")
            return HttpResponseRedirect('/')
        # request.session['email'] = email
        # request.session['password'] = password
        if email == 'admin9@arivani.net' and password == 'ar88iv08ni17':
            return redirect('/super-admin/')
        # return HttpResponseRedirect('/company/')
        Check_Company(email,password)

    return render(request,"login.html")
