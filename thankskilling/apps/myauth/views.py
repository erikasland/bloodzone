from django.shortcuts import render, redirect
from apps.myauth.models import User
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

def index(request):
    print 'hi from index in myauth'
    #del request.session['name']
    #print " all users: ", User.objects.all().values()
    if 'name' in request.session:
        print 'this is not working@@@@@', 
        return redirect('/movies')  
        #return render(request, 'myauth/success.html')
    else:
        print 'not yet #######3'
        return render(request, 'myauth/index.html')

def registration(request):
    print 'hi from reg in myauth'
    email = request.POST['email']
    date = datetime.now().strftime('%Y-%m-%d')
    password = request.POST['password']
    confirm = request.POST['confirm']
    name = request.POST['name']

    if not date or not password or not confirm or not email:
        return redirect('/')
    elif password != confirm:
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        return redirect('/')
    elif len(password) < 8:
        return redirect('/')
    
    count = User.objects.filter(email = email).count()
    if count >= 1:
        
        messages.add_message(request, messages.INFO, 'user is alreay registered')
        print 'already registered'
    else:
        new_user = User.objects.create(name = request.POST["name"], email = request.POST["email"], pw_hash = request.POST["password"], created_at = date, auto_auth = False)
        new_user.save()
        print 'new user'
        request.session['name'] = new_user.name
        request.session['id'] = new_user.id
        request.session['method'] = 'login'
    return redirect('/')

def login(request):
    print 'hi from login in myauth'
    email = request.POST['email']
    password = request.POST['password']
    #log_pass = User.objects.get(email = email).pw_hash
    log_user = User.objects.get(email = email)
    print 'log user info: ', log_user.pw_hash, log_user.email, log_user.name

    if not email or not password:
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        return redirect('/')
    elif log_user.pw_hash != password:
        return redirect('/') 
    elif log_user.auto_auth == True: 
        return redirect('/')
    else:
        request.session['name'] = log_user.name
        request.session['method'] = 'login'
        request.session['id'] = log_user.id
    return redirect('/')

def logout(request):
    print 'hi from logout in myauth'
    # del request.session['name']
    # del request.session['method']
    # del request.session['id']
    # del request.session['img']
    request.session.clear()
    return redirect('/')

def success(request):
    print 'hi from success in myauth'
    name = request.POST['name']
    image = request.POST['image']
    email = request.POST['email']
    date = datetime.now().strftime('%Y-%m-%d')
    user_id = 0
    count = User.objects.filter(email = email).count()
    if count >= 1:
        
        messages.add_message(request, messages.INFO, 'user is alreay registered')
        user_id = User.objects.get(email = email).id
        print 'already registered'
    else:
        new_user = User.objects.create(name = name, email = email, created_at = date, pw_hash = "password", auto_auth = True)
        new_user.save()
        user_id = new_user.id
        print 'new auth user'
    print "user id#### ", user_id
    info = {'name':name, 'image':image, 'email':email, 'uid':user_id}
    request.session['name'] = name
    request.session['method'] = 'auth'
    request.session['id'] = user_id
    request.session['img'] = image
    return redirect('/movies')
    #return render(request, 'myauth/success.html', info)
    #return redirect('index1',  info)
