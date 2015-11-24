from django.shortcuts import render

def index(request):
    print 11111111111111111111111
    return render(request, 'myauth/index.html')
