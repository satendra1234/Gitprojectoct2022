from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from account.models import Profile


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Account not Found')
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_varified:
            messages.warning(request, 'your account is not verified')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email, password=pwd)
        if user_obj:
            login(request, user_obj)
            return redirect('/')

        messages.warning(request, "Invalid Credentials")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'account/login.html')


def Register(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pwd = request.POST.get('password')

        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, 'Email is already exist')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name=f_name, last_name=l_name, email=email, username=email)
        user_obj.set_password(pwd)
        user_obj.save()

        messages.success(request, "An Email has been sent on your mail .")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'account/register.html')


def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_mail_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse("Invalid email token")