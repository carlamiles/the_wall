from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User
# Create your views here.
def index(request):
    print('the login and registration page is being displayed')
    return render(request, 'login_app_the_wall/index.html')

def success(request):
    print('currently displaying the success page!')
    if 'new_user_id' not in request.session: #this ensures that the user cannot see the success page without logging in
        return redirect('/')
    else:
        return render(request, 'login_app_the_wall/success.html', context)

def add_user(request):
    print('*'*50)
    print('the add user method is running!')
    print('password: ', request.POST["password_reg"])
    print('password conf: ', request.POST["confirm_password_reg"])
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        print('*'*50, 'creating user')
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email_address=request.POST["email"], password=request.POST["password_reg"], password_conf=request.POST["confirm_password_reg"])
        new_user = User.objects.last()
        request.session['new_user_id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        request.session['last_name'] = new_user.last_name
        return redirect('/wall')

def login(request):
    print('the login method is running')
    errors = User.objects.login_validator(request.POST)
    print('*'*50, errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        print('success method is running')
        user_match = User.objects.get(email_address=request.POST['email_log'], password=request.POST['password_log'])
        request.session['new_user_id'] = user_match.id
        request.session['first_name'] = user_match.first_name
        request.session['last_name'] = user_match.last_name
        print('*'*50, user_match)
        return redirect('/wall')

def logout(request):
    print('the logout method is running')
    request.session.clear()
    return redirect('/')